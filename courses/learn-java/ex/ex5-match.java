public class Match {

    //Variables
    private Squad homeSquad;
    private Squad visitorSquad;
    private int homeGoal = 0;
    private int visitorGoal = 0;

    //Constructor
    public Match(Squad homeSquad, Squad visitorSquad) {
        this.homeSquad = homeSquad;
        this.visitorSquad = visitorSquad;
    }

    //Get & Set method
    public Squad getHomeSquad() {
        return this.homeSquad;
    }

    public boolean setHomeSquad(Squad homeSquad) {
        boolean isVoidSquad = homeSquad.isEmpty();
        if(!isVoidSquad) {
            this.homeSquad = homeSquad;
        }
        return isVoidSquad;
    }

    public Squad getVisitorSquad() {
        return this.visitorSquad;
    }

    public boolean setVisitorSquad(Squad visitorSquad) {
        boolean isVoidSquad = visitorSquad.isEmpty();
        if(!isVoidSquad) {
            this.visitorSquad = visitorSquad;
        }
        return isVoidSquad;
    }

    public int getHomeGoal() {
        return this.homeGoal;
    }

    public boolean setHomeGoal(int homeGoal) {
        boolean isVoidInt = false;
        if(!isVoidInt) {
            this.homeGoal = homeGoal;
        }
        return isVoidInt;
    }

    public int getVisitorGoal() {
        return this.visitorGoal;
    }

    public boolean setVisitorGoal(int visitorGoal) {
        boolean isVoidInt = false;
        if(!isVoidInt) {
            this.visitorGoal = visitorGoal;
        }
        return isVoidInt;
    }

}