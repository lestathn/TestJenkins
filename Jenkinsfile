node {
    
  stage 'Checkout'

  git 'https://github.com/lestathn/TestJenkins.git'
        
  stage 'Package Docker image'

  def img = docker.build('coxauto/jenkins-docker-python-example:latest', '.')

    
  stage 'Run Test File'
  python -m unittest 
    //test name
    
  stage 'Publish'
  docker.withRegistry('https://nexus.doyouevenco.de', 'nexus-admin') {
     img.push('latest')
  }

}
  
