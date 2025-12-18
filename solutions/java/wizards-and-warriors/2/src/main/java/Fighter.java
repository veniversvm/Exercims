class Fighter {

    boolean isVulnerable() {
        return true;
    }

    int getDamagePoints(Fighter fighter) {
        return 1;
    }
}

class Warrior extends Fighter{

    @Override
    public String toString(){
        return "Fighter is a Warrior";
    }

    @Override
    public boolean isVulnerable() {
        return false;
    }

    @Override
    int getDamagePoints(Fighter fighter) {
        return fighter.isVulnerable() ? 10 : 6 ;
    }
}

class Wizard extends Fighter{
    boolean preparingSpell = false;
    
    @Override
    public String toString(){
        return "Fighter is a Wizard";
    }

    @Override
    public boolean isVulnerable() {
        return !preparingSpell;
    }

    void prepareSpell() {
        preparingSpell = !preparingSpell;
    }

    @Override
    int getDamagePoints(Fighter fighter) {
        return preparingSpell ? 12 : 3;
    }
}