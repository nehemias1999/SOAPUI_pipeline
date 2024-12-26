
import xml.etree.ElementTree as ET
import argparse

def convert_to_junit(input_file, output_file):
    tree = ET.parse(input_file)
    root = tree.getroot()

    # Crear el formato JUnit
    testsuite = ET.Element("testsuite", {
        "name": root.attrib["name"],
        "tests": root.attrib["tests"],
        "failures": root.attrib["failures"],
        "errors": root.attrib["errors"],
        "time": root.attrib["time"]
    })

    for testcase in root.findall("testcase"):
        # Crear cada <testcase>
        junit_testcase = ET.SubElement(testsuite, "testcase", {
            "name": testcase.attrib["name"],
            "classname": root.attrib["name"],
            "time": testcase.attrib["time"]
        })

        # Si hay fallo, agregar <failure>
        failure = testcase.find("failure")
        if failure is not None:
            junit_failure = ET.SubElement(junit_testcase, "failure", {
                "type": failure.attrib["type"],
                "message": failure.attrib["message"]
            })
            junit_failure.text = failure.text

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
