pipeline {

    agent any

    environment {
        WORKSPACE = "Desktop"
    }

    stages {

        stage('Run SOAPUI Test') {

            steps {

                script {

                    // Ejecutar el TestCase
                    def soapuiCommand = """
                    "C:\\Program Files\\SmartBear\\SoapUI-5.7.2\\bin\\testrunner.bat" -j -f "${WORKSPACE}\\results" -RJUnit "${WORKSPACE}\\ClienteCrear-soapui-project.xml"
                    """

                    sh soapuiCommand

                }

            }

        }

        stage('Publish Results') {

            steps {

                // Publicar resultados JUnit
                junit '**/results/*.xml'

            }

        }

    }

}
