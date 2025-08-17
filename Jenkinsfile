pipeline {
    agent any

    environment {
        // Jenkins credentials (add these in Jenkins -> Credentials)
        RECEIVER_EMAIL = credentials('RECEIVER_EMAIL')
        SMTP_SERVER    = credentials('SMTP_SERVER')
        SMTP_PORT      = credentials('SMTP_PORT')
        EMAIL_USER     = credentials('EMAIL_USER')
        EMAIL_PASSWORD = credentials('EMAIL_PASSWORD')
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                sh '''
                python3 -m pip install --upgrade pip
                pip3 install selenium webdriver-manager pytest pytest-html yagmail
                '''
            }
        }

        stage('Run Python Scripts & Generate Report') {
            steps {
                sh '''
                echo "Starting to run all Python scripts..."
                mkdir -p reports
                report_file="reports/report.html"

                echo "<html><body><h2>Python Scripts CI Report</h2><ul>" > $report_file

                for script in *.py; do
                  if [ -f "$script" ]; then
                    echo "Running $script..."
                    python3 "$script"
                    if [ $? -ne 0 ]; then
                      echo "<li><b>$script:</b> Failed</li>" >> $report_file
                    else:
                      echo "<li><b>$script:</b> Success</li>" >> $report_file
                    fi
                  fi
                done

                echo "</ul></body></html>" >> $report_file
                '''
            }
        }

        stage('Archive HTML Report') {
            steps {
                archiveArtifacts artifacts: 'reports/report.html', fingerprint: true
            }
        }

        stage('Send Report Email') {
            steps {
                sh '''
                python3 - <<EOF
import yagmail, os

receiver  = os.environ['RECEIVER_EMAIL']
smtp      = os.environ['SMTP_SERVER']
port      = int(os.environ['SMTP_PORT'])
user      = os.environ['EMAIL_USER']
password  = os.environ['EMAIL_PASSWORD']

subject="Python Scripts CI Report"
body="Hi,\\n\\nPlease find attached the latest Python scripts execution report."
filename="reports/report.html"

yag = yagmail.SMTP(user=user, password=password, host=smtp, port=port, smtp_ssl=True)
yag.send(to=receiver, subject=subject, contents=body, attachments=filename)
EOF
                '''
            }
        }
    }

    post {
        success {
            echo 'All Python scripts ran successfully and email sent!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
