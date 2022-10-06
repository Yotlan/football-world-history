import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class Match {

    //Variables
    private Squad homeSquad;
    private Squad visitorSquad;
    private List<String> startingHomePlayer;
    private List<String> startingVisitorPlayer;
    private List<Integer> homePosition;
    private List<Integer> visitorPosition;
    private int homeGoal = 0;
    private int visitorGoal = 0;

    //Constructor
    public Match(Squad homeSquad, List<Integer> homePosition, Squad visitorSquad, List<Integer> visitorPosition) {
        this.homeSquad = homeSquad;
        this.homePosition = homePosition;
        this.startingHomePlayer = new ArrayList<>();
        this.visitorSquad = visitorSquad;
        this.visitorPosition = visitorPosition;
        this.startingVisitorPlayer = new ArrayList<>();
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
        return !isVoidSquad;
    }

    public Squad getVisitorSquad() {
        return this.visitorSquad;
    }

    public boolean setVisitorSquad(Squad visitorSquad) {
        boolean isVoidSquad = visitorSquad.isEmpty();
        if(!isVoidSquad) {
            this.visitorSquad = visitorSquad;
        }
        return !isVoidSquad;
    }

    public int getHomeGoal() {
        return this.homeGoal;
    }

    public boolean setHomeGoal(int homeGoal) {
        boolean isVoidInt = false;
        if(!isVoidInt) {
            this.homeGoal = homeGoal;
        }
        return !isVoidInt;
    }

    public int getVisitorGoal() {
        return this.visitorGoal;
    }

    public boolean setVisitorGoal(int visitorGoal) {
        boolean isVoidInt = false;
        if(!isVoidInt) {
            this.visitorGoal = visitorGoal;
        }
        return !isVoidInt;
    }

    public List<String> getStartingHomePlayer() {
        return this.startingHomePlayer;
    }

    public boolean setStartingHomePlayer(List<String> startingHomePlayer) {
        boolean isVoidList = startingHomePlayer.isEmpty();

        List<String> GbHome = new ArrayList<>(homeSquad.getGoalkeepersList());
        List<String> DfHome = new ArrayList<>(homeSquad.getDefendersList());
        List<String> MtHome = new ArrayList<>(homeSquad.getMidfieldersList());
        List<String> AtHome = new ArrayList<>(homeSquad.getStrikersList());

        GbHome.retainAll(startingHomePlayer);
        DfHome.retainAll(startingHomePlayer);
        MtHome.retainAll(startingHomePlayer);
        AtHome.retainAll(startingHomePlayer);

        if(GbHome.size() != 1 && DfHome.size() != homePosition.get(0) && MtHome.size() != homePosition.get(1) && AtHome.size() != homePosition.get(2)) {
            return false;
        }

        if(!isVoidList && startingHomePlayer.size() == 11) {
            this.startingHomePlayer = startingHomePlayer;
        }
        return !isVoidList;
    }

    public List<String> getStartingVisitorPlayer() {
        return this.startingVisitorPlayer;
    }

    public boolean setStartingVisitorPlayer(List<String> startingVisitorPlayer) {
        boolean isVoidList = startingVisitorPlayer.isEmpty();

        List<String> GbVisitor = new ArrayList<>(visitorSquad.getGoalkeepersList());
        List<String> DfVisitor = new ArrayList<>(visitorSquad.getDefendersList());
        List<String> MtVisitor = new ArrayList<>(visitorSquad.getMidfieldersList());
        List<String> AtVisitor = new ArrayList<>(visitorSquad.getStrikersList());

        GbVisitor.retainAll(startingVisitorPlayer);
        DfVisitor.retainAll(startingVisitorPlayer);
        MtVisitor.retainAll(startingVisitorPlayer);
        AtVisitor.retainAll(startingVisitorPlayer);

        if(GbVisitor.size() != 1 && DfVisitor.size() != visitorPosition.get(0) && MtVisitor.size() != visitorPosition.get(1) && AtVisitor.size() != visitorPosition.get(2)) {
            return false;
        }
        if(!isVoidList && startingVisitorPlayer.size() == 11) {
            this.startingVisitorPlayer = startingVisitorPlayer;
        }
        return !isVoidList;
    }

    //Methods
    public boolean play() {
        boolean notStartMatch = this.startingHomePlayer.isEmpty() || this.startingVisitorPlayer.isEmpty();
        if(notStartMatch) {
            return notStartMatch;
        }
        //Create view for each post in each Squad
        List<String> GbHome = this.startingHomePlayer.subList(0,1);
        List<String> DfHome = this.startingHomePlayer.subList(1,this.homePosition.get(0)+1);
        List<String> MtHome = this.startingHomePlayer.subList(this.homePosition.get(0)+1,this.homePosition.get(0)+this.homePosition.get(1)+1);
        List<String> AtHome = this.startingHomePlayer.subList(this.homePosition.get(0)+this.homePosition.get(1)+1,this.homePosition.get(0)+this.homePosition.get(1)+this.homePosition.get(2)+1);

        List<String> GbVisitor = this.startingVisitorPlayer.subList(0,1);
        List<String> DfVisitor = this.startingVisitorPlayer.subList(1,this.visitorPosition.get(0)+1);
        List<String> MtVisitor = this.startingVisitorPlayer.subList(this.visitorPosition.get(0)+1,this.visitorPosition.get(0)+this.visitorPosition.get(1)+1);
        List<String> AtVisitor = this.startingVisitorPlayer.subList(this.visitorPosition.get(0)+this.visitorPosition.get(1)+1,this.visitorPosition.get(0)+this.visitorPosition.get(1)+this.visitorPosition.get(2)+1);

        System.out.println("Start Match");
        for(int i=0; i<=90; i++) {
            System.out.print(i + "'");
            double action = Math.random();
            //If action < 0.3 : home gb save
            if(action < 0.3) {
                //If action < 0.2 : visitor Squad scored
                if (action < 0.025) {
                    System.out.print(" Goal for " + this.visitorSquad.getSquadName() + " ! " + AtVisitor.get(new Random().nextInt(AtVisitor.size())) + " scored !");
                    this.visitorGoal++;
                } else {
                    System.out.print(" " + this.homeSquad.getSquadName() + " goalkeeper " + GbHome.get(0) + " save the ball ! ");
                }
            }
            //If action > 0.4 and < 0.5 : home event !
            if(action > 0.4 && action < 0.5) {
                /*
                0 : Penalty against home Squad
                1 : home Defender save the ball
                2 : home Defender pass the ball to a home midfielder
                 */
                int event = new Random().nextInt(3);
                switch(event) {
                    case 0:
                        System.out.print(" Fault from " + this.startingHomePlayer.get(new Random().nextInt(11)) + " on " + this.startingVisitorPlayer.get(new Random().nextInt(11)) + " ! " + AtVisitor.get(new Random().nextInt(AtVisitor.size())) + " go in front of " + GbHome.get(0) + " to try to scored and ...");
                        if(Math.random() > 0.5) {
                            System.out.print(" scored !!!");
                            this.visitorGoal++;
                        } else {
                            System.out.print(" missed !");
                        }
                        break;
                    case 1:
                        System.out.print(" " + DfHome.get(new Random().nextInt(DfHome.size())) + " save the ball !");
                        break;
                    case 2:
                        System.out.print(" " + DfHome.get(new Random().nextInt(DfHome.size())) + " pass to " + MtHome.get(new Random().nextInt(MtHome.size())));
                        break;
                }
            }
            //If action > 0.7 : visitor gb save
            if(action > 0.7) {
                //If action > 0.8 : home Squad scored
                if(action > 0.975) {
                    System.out.print(" Goal for " + this.homeSquad.getSquadName() + " ! " + AtHome.get(new Random().nextInt(AtHome.size())) + " scored !");
                    this.homeGoal++;
                } else {
                    System.out.print(" " + this.visitorSquad.getSquadName() + " goalkeeper " + GbVisitor.get(0) + " save the ball ! ");
                }
            }
            //If action < 0.6 and > 0.5 : visitor event !
            if(action < 0.6 && action > 0.5) {
                /*
                0 : Penalty against visitor Squad
                1 : visitor Defender save the ball
                2 : visitor Defender pass the ball to a visitor midfielder
                 */
                int event = new Random().nextInt(3);
                switch(event) {
                    case 0:
                        System.out.print(" Fault from " + this.startingVisitorPlayer.get(new Random().nextInt(11)) + " on " + this.startingHomePlayer.get(new Random().nextInt(11)) + " ! " + AtHome.get(new Random().nextInt(AtHome.size())) + " go in front of " + GbVisitor.get(0) + " to try to scored and ...");
                        if (Math.random() > 0.5) {
                            System.out.print(" scored !!!");
                            this.visitorGoal++;
                        } else {
                            System.out.print(" missed !");
                        }
                        break;
                    case 1:
                        System.out.print(" " + DfVisitor.get(new Random().nextInt(DfVisitor.size())) + " save the ball !");
                        break;
                    case 2:
                        System.out.print(" " + DfVisitor.get(new Random().nextInt(DfVisitor.size())) + " pass to " + MtVisitor.get(new Random().nextInt(MtVisitor.size())));
                        break;
                }
            }
            System.out.print("\n");
        }
        System.out.println("Match End");
        System.out.println(this.homeSquad.getSquadName() + " : " + this.homeGoal);
        System.out.println(this.visitorSquad.getSquadName() + " : " + this.visitorGoal);
        return true;
    }

}