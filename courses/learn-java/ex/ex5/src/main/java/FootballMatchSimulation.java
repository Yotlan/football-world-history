import java.util.Arrays;
import java.util.ArrayList;

public class FootballMatchSimulation {
    public static void main(String[] args) {

        //Create the first squad : Manchester United

        //Squad member Array
        String[] manchesterUtdGblist = {"David de Gea", "Dean Henderson", "Nathan Bishop", "Lee Grant"};
        String[] manchesterUtdDfList = {"Aaron Wan-Bissaka", "Harry Maguire", "Luke Shaw", "Victor Lidelof", "Eric Bailly", "Alex Telles", "Axel Tuanzebe", "Brandon Williams", "Timothy Fosu-Mensah", "William Thomas Fish"};
        String[] manchesterUtdMtList = {"Bruno Fernandes", "Fred", "Scott McTominay", "Paul Pogba", "Nemanja Matic", "Juan Mata", "Donny van de Beek", "Hannibal Menjbri", "Jesse Lingard"};
        String[] manchesterUtdAtList = {"Marcus Rashford", "Paul Pogba", "Mason Greenwood", "Anthony Martial", "Edison Cavani", "Daniel James", "Juan Mata", "Donny van de Beek", "Amad Diallo", "Anthony Elanga", "Shola Shoretire", "Odion Ighalo", "Jesse Lingard"};

        //Squad Object
        Squad manchesterUtd = new Squad(
                new ArrayList<>(Arrays.asList(manchesterUtdGblist)),
                new ArrayList<>(Arrays.asList(manchesterUtdDfList)),
                new ArrayList<>(Arrays.asList(manchesterUtdMtList)),
                new ArrayList<>(Arrays.asList(manchesterUtdAtList)),
                "Manchester United",
                "Ole Gunnar Solskjaer"
        );

        //Create the second squad : Manchester City

        //Squad member Array
        String[] manchesterCityGbList = {"Ederson", "Scott Carson", "Zack Steffen", "James Trafford"};
        String[] manchesterCityDfList = {"Ruben Dias", "Joao Cancelo", "Kyle Walker", "John Stones", "Oleksandr Zinchenko", "Aymeric Laporte", "Benjamin Mendy", "Nathan Aké", "Eric Garcia", "Taylor Harwood-Bellis", "Luke Mbete-Tatu", "Nicolas Otamendi"};
        String[] manchesterCityMtList = {"Rodri", "Bernardo Silva", "Ilkay Gundogan", "Kevin De Bruyne", "Phil Foden", "Ferran Torres", "Fernandinho", "Sergio Aguero", "Adrian Bernabe", "Thomas Doyle", "Claudio Gomes", "Felix Kalu Nmecha", "Cole Palmer"};
        String[] manchesterCityAtList = {"Raheem Sterling", "Bernardo Silva", "Riyad Mahrez", "Gabriel Jesus", "Phil Foden", "Ferran Torres", "Sergio Aguero", "Liam Delap"};

        //Squad Object
        Squad manchesterCity = new Squad(
                new ArrayList<>(Arrays.asList(manchesterCityGbList)),
                new ArrayList<>(Arrays.asList(manchesterCityDfList)),
                new ArrayList<>(Arrays.asList(manchesterCityMtList)),
                new ArrayList<>(Arrays.asList(manchesterCityAtList)),
                "Manchester City",
                "Pep Guardiola"
        );

        //Position
        Integer[] manchesterUtdPosition = {4, 4, 2};
        Integer[] manchesterCityPosition = {4, 3, 3};

        //Match Object
        Match manchesterDerby = new Match(
                manchesterUtd,
                new ArrayList<>(Arrays.asList(manchesterUtdPosition)),
                manchesterCity,
                new ArrayList<>(Arrays.asList(manchesterCityPosition))
        );

        String[] manchesterUtdStartingSquad = {"David de Gea", "Aaron Wan-Bissaka", "Harry Maguire", "Luke Shaw", "Victor Lidelof", "Bruno Fernandes", "Fred", "Scott McTominay", "Paul Pogba", "Marcus Rashford", "Mason Greenwood"};
        String[] manchesterCityStartingSquad = {"Ederson", "Ruben Dias", "Joao Cancelo", "Kyle Walker", "John Stones", "Rodri", "Bernardo Silva", "Ilkay Gundogan", "Raheem Sterling", "Bernardo Silva", "Riyad Mahrez"};

        manchesterDerby.setStartingHomePlayer(Arrays.asList(manchesterUtdStartingSquad));
        manchesterDerby.setStartingVisitorPlayer(Arrays.asList(manchesterCityStartingSquad));

        manchesterDerby.play();

    }
}