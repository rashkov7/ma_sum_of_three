pipeline {
  agent any
  stages {
      stage('AWS') {
        agent {
            docker {
                image 'amazon/aws-cli'
            }
        }
        steps {
          echo 'Testing AWS'
          sh '''
          touch build/index.html
          '''
        }

        stage('Building') {
        steps {
          echo 'Running build stage'
          sh '''
          touch build/index.html
          '''
        }
      }
      stage('Test') {
        steps {
           echo 'Running Test stage'
           sh '''
           if [ -f build/index.html ];
            then
                 exit 0
            else
                exit 1
           fi
           '''
        }
      }
  }
}
