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
                    // def soapuiCommand = """
                    // "C:\\Program Files\\SmartBear\\SoapUI-5.7.2\\bin\\testrunner.bat" -j -f "${WORKSPACE}\\results" -RJUnit "${WORKSPACE}\\ClienteCrear-soapui-project.xml"
                    // """

                    // sh soapuiCommand

                    bat label: 'Ejecucion de test',
                    script: '"C:\\Program Files\\SmartBear\\SoapUI-5.7.2\\bin\\testrunner.bat" -j -f "Desktop\\results" -RJUnit "Desktop\\ClienteCrear-soapui-project.xml"'

                }

            }

        }

        // stage('Publish Results') {

        //     steps {

        //         // Publicar resultados JUnit
        //         junit '**/results/*.xml'

        //     }

        // }

    }

}
