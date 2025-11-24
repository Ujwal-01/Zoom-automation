pipeline {
    agent any
    stages {

        stage('Clone Repo') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Ujwal-01/Zoom-automation.git'
            }
        }

        stage('Install Python Dependencies') {
            steps {
                echo "Installing Python dependencies..."
                sh '''
                python3 --version
                pip3 install -r requirements.txt || pip install -r requirements.txt
                '''
            }
        }

        stage('Run Zoom Automation') {
            steps {
                sh 'chmod +x run.sh'
                sh './run.sh'
            }
        }
    }
}