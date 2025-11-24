pipeline {
    agent any
    stages {

        stage('Clone Repo') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Ujwal-01/Zoom-automation.git'
            }
        }

        stage('Install Python & pip') {
            steps {
                echo "Installing Python and pip if missing..."
                sh '''
                    # Install Python if missing
                    if ! command -v python3 &>/dev/null; then
                        echo "Python3 not found. Installing..."
                        sudo apt update
                        sudo apt install -y python3
                    fi

                    # Install pip if missing
                    if ! command -v pip3 &>/dev/null; then
                        echo "pip3 not found. Installing..."
                        sudo apt install -y python3-pip
                    fi

                    python3 --version
                    pip3 --version
                '''
            }
        }

        stage('Install Project Requirements') {
            steps {
                echo "Installing Python dependencies..."
                sh '''
                    # Install venv module if missing
                    sudo apt install -y python3-venv

                    # Create virtual environment
                    if [ ! -d "venv" ]; then
                        python3 -m venv venv
                    fi

                    # Activate environment and install requirements
                    source venv/bin/activate
                    pip3 install --upgrade pip
                    pip3 install -r requirements.txt
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