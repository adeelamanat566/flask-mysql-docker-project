pipeline { 
    agent any
    stages {
        stage('build'){
            steps {
            sh 'docker compose build'
            sh 'docker compose ps'
            
            }
        }
        stage('TESTING'){
            steps {
                echo 'Starting application...' 
                sh 'docker compose up -d' 
                echo 'Testing application...' 
                sh 'curl -f http://localhost:5000'            
            }
        
        }
        stage('continues') {
            steps {
                input(
                    message: 'continues',
                    ok: 'yesy conti'

                
                
                )
                
                
                
            
            
            }
        
        
        }
        stage('deploy'){
            steps {
                sh 'docker compose up -d'
            
            
            }
        
        }
    
    }
    post {
        always {
            echo "running "
        }
        success {
            echo "success"
        }
        failure {
            echo "faile"
        }
    
    
    
    
    
    }
    
    
}
