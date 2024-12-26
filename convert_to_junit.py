
import xml.etree.ElementTree as ET
import argparse

def convert_to_junit(input_file, output_file):
    tree = ET.parse(input_file)
    root = tree.getroot()

    # Crear el formato JUnit
    testsuite = ET.Element('testsuite')
    testsuite.attrib['name'] = root.attrib.get('name', 'TestSuite')
    testsuite.attrib['tests'] = root.attrib.get('name', 'tests')
    testsuite.attrib['failures'] = root.attrib.get('name', 'failures')
    testsuite.attrib['errors'] = root.attrib.get('name', 'errors')
    testsuite.attrib['skipped'] = '0'

    for testcase in root.findall('testcase'):
        junit_testcase = ET.SubElement(testsuite, 'testcase')
        junit_testcase.attrib['classname'] = testcase.attrib.get('name', 'UnnamedTestCase')
        junit_testcase.attrib['name'] = testcase.attrib.get('name', 'UnnamedTestStep')
        junit_testcase.attrib['time'] = testcase.attrib.get('time', '0')

        # Agregar fallos como <failure>
        for assertion in testcase.findall(".//assertion[@status='FAILED']"):
            failure = ET.SubElement(junit_testcase, 'failure')
            failure.attrib['message'] = assertion.text or 'Assertion failed'
            failure.text = 'Detalles del fallo'

    # Guardar el resultado en formato JUnit
    tree = ET.ElementTree(testsuite)
    tree.write(output_file, encoding='utf-8', xml_declaration=True)

if __name__ == "__main__":
    # Configurar el parser de argumentos
    parser = argparse.ArgumentParser(description="Convertir reportes de SOAPUI a formato JUnit.")
    parser.add_argument("input_file", help="Ruta al archivo XML de entrada.")
    parser.add_argument("output_file", help="Ruta al archivo XML de salida en formato JUnit.")

    # Leer argumentos
    args = parser.parse_args()

    # Llamar a la función con los argumentos proporcionados
    convert_to_junit(args.input_file, args.output_file)
