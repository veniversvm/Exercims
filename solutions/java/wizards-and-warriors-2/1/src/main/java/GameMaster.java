public class GameMaster {

    public String describe(Character character) {
        return "You're a level " + character.getLevel() + " " + character.getCharacterClass() + " with " + character.getHitPoints() +" hit points.";
    }

    public String describe(Destination destination) {
        return "You've arrived at " + destination.getName() + ", which has " + destination.getInhabitants() +  " inhabitants.";
    }

    public String describe(TravelMethod travelMethod) {
         String travel = travelMethod == TravelMethod.WALKING ? "by walking" : "on horseback";
         return "You're traveling to your destination " + travel + ".";
    }

    // TODO: define a 'describe' method that returns a description of a Character, Destination and TravelMethod
    public String describe(Character character, Destination destination, TravelMethod travelMethod) {
         return this.describe(character) + " " + this.describe(travelMethod) + " "+ this.describe(destination);
    }

     public String describe(Character character, Destination destination) {
         return this.describe(character) + " You're traveling to your destination by walking. "+ this.describe(destination);
    }
}
