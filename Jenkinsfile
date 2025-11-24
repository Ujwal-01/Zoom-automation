pipeline {
    agent any

    stages {

        stage('Clone Repo') {
            steps {
                git url: 'https://github.com/Ujwal-01/Zoom-automation.git', branch: 'main'
            }
        }

        stage('Prepare Environment') {
            steps {
                sh '''
                sudo apt update
                sudo apt install -y python3 python3-venv

                chmod +x run.sh
                '''
            }
        }

        stage('Run Automation Script') {
            steps {
                sh './run.sh'
            }
        }
    }

    post {
        success { echo "Pipeline Completed Successfully!" }
        failure { echo "Pipeline Failed — check logs above." }
    }
}
