public class FootballMatchReports {    
    public static String onField(int shirtNum) {
        switch (shirtNum) {
            case 1:
                return "goalie";
            case 2: 
                return "left back"; 
            case 3: case 4: // could also be --> case 3, 4: case body
                return "center back";
            case 5: 
                return "right back";
            case 6: case 7: case 8: // could also be --> case 6, 7, 8: case body
                return "midfielder";
            case 9: 
                return "left wing";
            case 10: 
                return "striker";
            case 11: 
                return "right wing";
            default: 
                throw new IllegalArgumentException();
        }
    }
}
