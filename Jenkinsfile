pipeline {

    agent any

    environment {

        WORKSPACE = "Desktop"

        PYTHONEXE = "C:\\Users\\nsalazar\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\venv\\scripts\\nt\\python.exe"

    }

    stages {

        stage('Run SOAPUI Test') {

            steps {

                script {

                    // bat label: 'Ejecucion de test',
                    // script: '"C:\\Program Files\\SmartBear\\SoapUI-5.7.2\\bin\\testrunner.bat" -j -r -f "C:\\Users\\nsalazar\\Desktop\\results" "C:\\Users\\nsalazar\\Desktop\\ClienteCrear-soapui-project.xml"'

                    bat label: 'Conversion a formato JUnit',
                    script: '"C:\\Users\\nsalazar\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\venv\\scripts\\nt\\python.exe" "convert_to_junit.py" "C:\\Users\\nsalazar\\Desktop\\results\\TEST-TestSuite_1.xml" "C:\\Users\\nsalazar\\Desktop\\results\\junit-result.xml"'

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
