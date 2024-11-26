pipeline {
  agent any
  stages {
       stage('Parallel Stage') {
        parallel {
            stage('Task 1') {
                steps {
                    echo 'Running Task 1'
                }
            }
            stage('Task 2') {
                agent{
                    docker{
                        image 'node:18-alpine'
                    }
                }
                steps {
                    echo 'Running Task 2'
                }
            }
        }
    }
  }
}
