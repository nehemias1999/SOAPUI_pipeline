
import xml.etree.ElementTree as ET

def convert_to_junit(input_file, output_file):
    tree = ET.parse(input_file)
    root = tree.getroot()

    # Crear el formato JUnit
    testsuite = ET.Element('testsuite')
    testsuite.attrib['name'] = root.attrib.get('name', 'TestSuite')
    testsuite.attrib['tests'] = str(len(root.findall('testcase')))
    testsuite.attrib['failures'] = str(len(root.findall(".//assertion[@status='FAILED']")))
    testsuite.attrib['errors'] = '0'
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

# Ejemplo de uso
convert_to_junit('C:\\ruta\\a\\resultados\\soapui-result.xml', 'C:\\ruta\\a\\resultados\\junit-result.xml')
