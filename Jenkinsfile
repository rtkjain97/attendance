pipeline {
        environment {
    registry = "rtkjain/atdsystem"
    registryCredential = 'docker-hub-credentials'
    dockerImage = ''
    dockerImageLatest = ''
  }
      agent any
      stages {
            stage('Init') {
                  steps {
                          logstash{
                        echo 'Hi, this is Ritik Jain'
                        echo 'I am executing Attendance system using pipeline'
                          }
                  }
            }
                stage('Cloning Git') {
      steps {
              logstash{
        git 'https://github.com/rtkjain97/attendance.git'
              }
      }
    }

            stage('Build') {
                  steps {
                          logstash{
                        echo 'building'
                          }
                  }

            }
            stage('Building image') {
      steps{
              logstash {
                sh "pwd"
                sh "ls -a"
        script {
          dockerImage = docker.build registry + ":$BUILD_NUMBER"
          dockerImageLatest = docker.build registry + ":latest"
        }
              }
      }
    }   
    stage('Deploy Image') {
      steps{
              logstash{
        script {
          docker.withRegistry( '', registryCredential ) {
            dockerImage.push()
            dockerImageLatest.push()
          }
        }
              }
      }
    }
    stage('Remove Unused docker image') {
      steps{
              logstash{
        sh "docker rmi $registry:$BUILD_NUMBER"
              }
      }
    }   
        stage('Execute Rundeck job') {
        steps {
                logstash{
          script {
            step([$class: "RundeckNotifier",
                  includeRundeckLogs: true,
                  jobId: "4811f41b-846e-4168-8974-cbd320c57a5c",
                  rundeckInstance: "Rundeck",
                  shouldFailTheBuild: true,
                  shouldWaitForRundeckJob: true,
                  tailLog: true])
            //echo "Rundeck JOB goes here"
          }
                }
        }
    }
}
}
