pipeline {
    agent any

    stages {
        stage('Setup & Install') {
            steps {
                sh '''
                    set -e
                    rm -rf venv
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirement.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
                    sh '''
                        set -e
                        source venv/bin/activate
                        behave -f allure_behave.formatter:AllureFormatter -o allure-results || true
                        echo "--- Contents of allure-results ---"
                        ls -lah allure-results
                    '''
                }
            }
        }

        stage('Generate Allure Report') {
            steps {
                sh '''
                    set -e
                    source venv/bin/activate
                    which allure || echo "Allure CLI not found"
                    allure generate allure-results -o allure-report --clean
                    echo "--- Contents of allure-report ---"
                    ls -lah allure-report
                '''
                archiveArtifacts artifacts: 'allure-report/**', allowEmptyArchive: true
            }
        }
    }

    post {
        always {
            // Publish Allure Report if the plugin is installed
            allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
        }
    }
}
