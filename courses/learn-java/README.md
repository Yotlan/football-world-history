# JAVA COURSES

## TABLE OF CONTENTS

## INSTALLATION ON WINDOWS 10

Follow theses steps to install java on your computer :
- Go on this link (<https://www.oracle.com/java/technologies/downloads/>)
- Download the JDK depending on your OS
- When it's download, launch the installer
- Take care where your JDK is installing (something like this : `C:\ProgramFiles\Java\jdk-18.0.1\`)
- Copy the path where your JDK are install (something like this : `C:\ProgramFiles\Java\jdk-18.0.1\bin`)
- Launch the **Edit the system environment variable** application (type Environment variable on your search bar)

![alt text](/courses/learn-java/img/capture_1.png)

- Click on environment variable (the last button)
- In *system variables*, find path, click on it and then click on the `Edit` button
- Click `New` and paste your JDK installing folder (something like this : `C:\ProgramFiles\Java\jdk-18.0.1\bin`)
- Click `OK`
- In *user variables for __username__*
- Click `New`
- In *variable name* field, put *JAVA_HOME*
- In *variable value* field, put your JDK installing folder, but with not `\bin` at the end (something like this : `C:\ProgramFiles\Java\jdk-18.0.1\`)
- Click `OK`
- Click `OK`
- Launch the **Command Prompt** application (type cmd on your search bar)
- Enter the following command in your cmd : `javac -version` and see if your cmd return your JDK version