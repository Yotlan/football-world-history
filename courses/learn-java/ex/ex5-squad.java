import java.util.ArrayList;
import java.util.List;

public class Squad {

    //Variables
    private List<String> goalkeepersList;
    private List<String> defendersList;
    private List<String> midfieldersList;
    private List<String> strikersList;
    private String squadName;
    private String managerName;
    
    //Constructor
    public Squad(List<String> goalkeepersList, List<String> defendersList, List<String> midfieldersList, List<String> strikersList, String squadName, String managerName) {
        this.goalkeepersList = goalkeepersList;
        this.defendersList = defendersList;
        this.midfieldersList = midfieldersList;
        this.strikersList = strikersList;
        this.squadName = squadName;
        this.managerName = managerName;
    }

    //Get & Set method
    public List<String> getGoalkeepersList() {
        return this.goalkeepersList;
    }

    public boolean setGoalkeepersList(List<String> goalkeepersList) {
        boolean isVoidList = goalkeepersList.isEmpty();
        if(!isVoidList) {
            this.goalkeepersList = goalkeepersList;
        }
        return isVoidList;
    }

    public List<String> getDefendersList() {
        return this.defendersList;
    }

    public boolean setDefendersList(List<String> defendersList) {
        boolean isVoidList = defendersList.isEmpty();
        if(!isVoidList) {
            this.defendersList = defendersList;
        }
        return isVoidList;
    }

    public List<String> getMidfieldersList() {
        return this.midfieldersList;
    }

    public boolean setMidfieldersList(List<String> midfieldersList) {
        boolean isVoidList = midfieldersList.isEmpty();
        if(!isVoidList) {
            this.midfieldersList = midfieldersList;
        }
        return isVoidList;
    }

    public List<String> getStrikersList() {
        return this.strikersList;
    }

    public List<String> setStrikersList(List<String> strikersList) {
        boolean isVoidList = strikersList.isEmpty();
        if(!isVoidList) {
            this.strikersList = strikersList;
        }
        return isVoidList;
    }

    public String getSquadName() {
        return this.squadName;
    }

    public boolean setSquadName(String squadName) {
        boolean isVoidString = squadName.isBlank();
        if(!isVoidString) {
            this.squadName = squadName;
        }
        return isVoidString;
    }

    public String getManagerName() {
        return this.managerName;
    }

    public boolean setManagerName(String managerName) {
        boolean isVoidString = managerName.isBlank();
        if(!isVoidString) {
            this.managerName = managerName;
        }
        return isVoidString;
    }

}