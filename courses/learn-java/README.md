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

Follow these steps to install java on your computer (also work for Ubuntu built-in Windows 10):
- Launch the **Terminal** application (type terminal on your search bar)
- Enter the following command in your terminal : `sudo apt update` to update all what we need an update
- Enter the following command in your terminal : `sudo apt install openjdk-18-jdk` to install the last JDK version
- Enter the following command in your terminal : `javac -version` and see if your terminal return your JDK version
- If the version return by the previous command is not your installing JDK version, enter the following command in your terminal : `sudo update-alternatives --config java` and enter the number corresponding to your JDK version (something like this : `/usr/lib/jvm/java-18-openjdk-amd64/bin/java`)

## CHOOSE AN IDE

I recommand you to choose the IDE (Software to write, read and launch code) in this following list :
- IntelliJ IDEA (<https://www.jetbrains.com/fr-fr/idea/download/#section=windows> and choose the version corresponding to your OS)
- Eclipse IDE (<https://www.eclipse.org/downloads/>)
- Visual Studio Code (<https://code.visualstudio.com/download> and choose the version corresponding to your OS)

To simplify the learning of java, the IDE choosen now is Visual Studio Code.

## GETTING START

### EXERCICE 1

The first exercice is simple : write in your terminal "Hello World !". It's important to know that java work with class. So create a first class who be your main class. After that, your main function who are launch by executing your java file (containing only 1 class) look like this :

```java
public static void main(String[] args) {
    //Some code...
}
```

After you doing this, you can use print command from `System.out` and print your message. To conclude, launch your java file by execute the following command in your terminal (here we launch the command in our IDE terminal (On Visual Studio Code, the terminal is available with the button `Terminal` and choose `New Terminal`) ). You can see this in your terminal :

```sh
java ex1.java
> Hello World !
```

The correction of this exercice are available at `ex/ex1.java`

### EXERCICE 2

The second exercice is about variable. It's very important to use variable, because you can update them when you want. For example, if you want to write all integer between 1 and 10, you can use a variable. So, instead of using 10 print method, you can use a for loop (or a while loop). A for loop in java look like this :

```java
for(int i=0; i<10; i++){
    //Some code...
}
```

And a while loop look like this :

```java
while(i<10){
    //Some code...
    i++;
}
```

Ton conclude this exercice, you need to write in the terminal like the previous exercice and then launch your program with this command :

```sh
java ex2.java
> 0
> 1
> 2
> 3
> 4
> 5
> 6
> 7
> 8
> 9
```

The correction of this exercice are available at `ex/ex2.java`

### EXERCICE 3

Now, you know variables. It's very usefull to use a value who will be update by another part of the code (like a for loop). Here you can have an example of some type you can use in your code :

| Type          | Example                        |
|---------------|--------------------------------|
| String        | "Hello World !"                |
| int           | 42                             |
| float         | 3.14                           |
| boolean       | true                           |

Something which are very usefull, is to use some operation like + to concatenate 2 words. With integer and float, it's a simple addition. But you cannot do that with boolean. In this exercice, you need to use what we use before, but with some operation like + or - for integer and float, + for string and `and`or `or` for boolean. Before you start this exercice, we introduce very quickly :

- and

| Operation       | Result          |
|-----------------|-----------------|
| true and true   | true            |
| true and false  | false           |
| false and true  | false           |
| false and false | false           |

- or

| Operation       | Result          |
|-----------------|-----------------|
| true or true    | true            |
| true or false   | true            |
| false or true   | true            |
| false or false  | false           |