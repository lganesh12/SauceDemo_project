pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh '''
                rm -rf venv
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }
        stage('Test') {
            steps {
                catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
                    sh '''
                    . venv/bin/activate
                    behave -f allure_behave.formatter:AllureFormatter -o allure-results
                    '''
                }
            }
        }
        stage('Allure Report') {
            steps {
                sh '''
                . venv/bin/activate
                allure generate allure-results -o allure-report --clean
                '''
                // Archive the report as a build artifact
                archiveArtifacts artifacts: 'allure-report/**', allowEmptyArchive: true
            }
        }
    }
    post {
        always {
            // If you have the Allure Jenkins plugin, this will publish the report and provide a link
            allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
        }
    }
}
