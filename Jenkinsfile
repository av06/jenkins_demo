pipeline {
    agent any
    parameters {
	choice (
		name: 'Proceed_Permission',
		choices: ['Proceed' , 'Stop'],
		description: ''
		)
	}
    stages {
	stage('Clean WS'){
	    steps {
		cleanWs()
		sh 'ls'
	    }
	}
	stage('SCM'){
	    steps {
		checkout scm
		sh 'ls'
	    }
	}
	stage('build') {
	    steps {
		withEnv(["HOME=${env.WORKSPACE}"]) {
		    echo '#####-Beginnig Build-#####'
		    sh 'python3 -m virtualenv my_env'   // Setting Up Python Virtual Environment
		    sh '. my_env/bin/activate'   // Activating Python Virtual Environment
		    sh 'pip3 install --user -r requirements.txt'   // Installing Required Python Modules
		    echo '#####-Build Complete-#####'
		}
	    }
	}
	stage('test') {
	    when{
		expression {
		    params.Proceed_Permission == 'Proceed'
		}
	    }
	    steps {
		withEnv(["HOME=${env.WORKSPACE}"]) {
		    echo '#####-Beginnig Test-#####'
		    sh 'python3 lint.py'   // Checking the code quality by linting
		    sh 'python3 -m pytest'   // Testing the Functions
		    echo '#####-Test Complete-#####'
		}
	    }
	    // post {
	    //     // always {
	    //     //     junit 'test-reports/*.xml'
	    //     // }
	    // }    
	}
    }
}

