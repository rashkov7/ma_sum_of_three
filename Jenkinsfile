pipeline {
  agent any
  stages {
       stage('Parallel Stage') {
        parallel {
            stage('Building') {
                steps {
                    echo 'Running Task 1'
                }
            }
            stage('Test') {

                }
                steps {
                    echo 'Running Task 2'
                }
            }
        }
    }
  }
}
