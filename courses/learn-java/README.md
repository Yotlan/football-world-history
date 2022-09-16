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

The correction of this exercice is available at `ex/ex1.java`

### EXERCICE 2

The second exercice is about variable. It's very important to use variable, because you can update them when you want. For example, if you want to write all integer between 1 and 10, you can use a variable. So, instead of using 10 print method, you can use a for loop (or a while loop). A for loop in java look like this :

```java
for(int i=0; i<10; i++){
    //Some code...
}
```

And a while loop look like this :

```java
int i=0;

while(i<10){
    //Some code...
    i++;
}
```

To conclude this exercice, you need to write in the terminal like the previous exercice and then launch your program with this command :

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

The correction of this exercice is available at `ex/ex2.java`

### EXERCICE 3

Now, you know variables. It's very usefull to use a value who will be update by another part of the code (like a for loop). Here you can have an example of some type you can use in your code :

| Type          | Example                        |
|---------------|--------------------------------|
| String        | "Hello World !"                |
| int           | 42                             |
| float         | 3.14                           |
| boolean       | true                           |

Something which are very usefull, is to use some operation like + to concatenate 2 words. With integer and float, it's a simple addition. But you cannot do that with boolean. In this exercice, you need to use what we use before, but with some operation like + or - for integer and float, + for string and `and`, `or` or `not` for boolean. Before you start this exercice, we introduce boolean very quickly :

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

- not

| Operation       | Result          |
|-----------------|-----------------|
| not true        | false           |
| not false       | true            |

Boolean variables are very usefull if you want to check some condition. Instead, for example, in the previous for loop we saw in the last exercice, you can see `i<10`. This condition mean until i is lower than 10, you can continue the for loop (and increment i with `i++`). Now, in this exercice, what we want is that :

- print the addition between 4 and 2
- print the substraction between 3.14 and 1.5
- print the concatenation between "Hello " and "World !"
- all this printing line in a conditionnal loop (if) who check if the user use an arguments or not

To do this, you follow this pattern :
```java
public static void main(String[] args) {
    if(args.size > 0){
        //Some code...
    }
}
```

Now, if you run your program, you can see this:

```sh
java ex3.java
> 
java ex3.java something
> 6
> 1.640000000000001
> Hello World !
```

The correction of this exercice is available at `ex/ex3.java`

#### TIPS

Something very boring when someone write code is when he use variable but with a strange name. For example, if you have a variable you use for a reference for the number of goal scored by Thierry Heny, but you named that variable `g`, only you can understand this ! The good way to named your variable is to named it like this `ThierryHenryGoal`. Like this, everyone understand the meaning of this variable : the number of goal scored by Thierry Henry.

#### IMPORTANT INFORMATIONS : DATA TYPES

Before you continu this courses, you need to learn by heart this graphics bellow :

![data-type](/courses/learn-java/img/java-data-types.jpg)

This graphics is very important because if a type is primitives, you don't need to import his packages to use it (like int, float, boolean, ...). But if you use some non-primitives types, you need to import his packages like this :

```java
import java.util.ArrayList;

public class Main {
    //Some code ...
}
```

The package we import is for ArrayList. With this data-type, you can now have a better table (better than String[] or Integer[]). Some package are directly import by default in java, like for the package String (who are in java.lang which is directly imported in java). So, it's very important to search the package to import if you want to use some non-primitives data types.

### EXERCICE 4

Something very usefull is type casting. Indeed, sometime you need to cast a type to another (for example an int to a double or a char to a string). They exist 2 types of type casting : 
- Widening Casting : converting a smaller type to a larger one
- Narrowing Casting : converting a larger type to a smaller one

Widening Castings are doing automaticly, but not for Narrowing Casting who you need to do it manually. Indeed, in Widening Casting, you don't loose any information because you cast a smaller type to a larger one. But in Narrowing Casting, you loose some information. For example if you cast a float to an int, you loose all the number after the comma. In this exercice, you have to print with the same variable, an int and a float. To do this, you need to follow this schema : 

```java
float myFloatVar = 3.14;
int myIntVar = (int) myFloatVar; //Narrowing Casting
float myNewFloatVar = myIntVar; //Widening Casting

System.out.println(myFloatVar);
System.out.println(myIntVar);
System.out.println(myNewFloatVar);
```

Now, if you run your program, you can see this :
```sh
java ex4.java
> 3.14
> 3
> 3.0
```

The correction of this exercice is available at `ex/ex4.java`