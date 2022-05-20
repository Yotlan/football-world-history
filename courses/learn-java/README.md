# JAVA COURSES

## TABLE OF CONTENTS

## INSTALLATION

### ON WINDOWS 10

Follow these steps to install java on your computer :
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
- Enter the following command in your terminal : `javac -version` and see if your terminal return your JDK version

### ON LINUX

Follow these steps to install java on your computer :
- Launch the **Terminal** application (type terminal on your search bar)
- Enter the following command in your terminal : `sudo apt update` to update all what we need an update
- Enter the following command in your terminal : `sudo apt install openjdk-18-jdk` to install the last JDK version
- Enter the following command in your terminal : `javac -version` and see if your terminal return your JDK version
- If the version return by the previous command is not your installing JDK version, enter the following command in your terminal : `sudo update-alternatives --config java` and enter the number corresponding to your JDK version (something like this : `/usr/lib/jvm/java-18-openjdk-amd64/bin/java`)

## CHOOSE AN IDE

I recommand you to choose the IDE in this following list :
- IntelliJ IDEA (<https://www.jetbrains.com/fr-fr/idea/download/#section=windows> and choose the version corresponding to your OS)
- Eclipse IDE (<https://www.eclipse.org/downloads/>)
- Visual Studio Code (<https://code.visualstudio.com/download> and choose the version corresponding to your OS)

To simplify the learning of java, the IDE choosen now is Eclipse IDE.