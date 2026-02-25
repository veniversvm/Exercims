import java.util.List;
import java.util.ArrayList;
import java.util.Random;
import java.util.Collections;

class DnDCharacter {
    private int max = 6;
    private int min = 1;
    // Character stats
    private int hp = 10;
    private int str = 0;
    private int dxt = 0;
    private int cnst = 0;
    private int intl = 0;
    private int wsdm = 0;
    private int chrm = 0;

    public DnDCharacter() {
        this.str = getAbility();
        this.dxt = getAbility();
        this.intl = getAbility();
        this.wsdm = getAbility();
        this.chrm = getAbility();
        this.cnst  = getAbility();
    }

    private int getAbility() {
        List<Integer> scores = this.rollDice();
        return ability(scores);
    }

    int ability(List<Integer> scores) {
        int value = 0;
        for (int v : scores) {
            value += v;
        }

        return value - Collections.min(scores);
    }
    
    List<Integer> rollDice() {
        Random random = new Random();
        List<Integer> rollList = new ArrayList<>();
        for (int i = 0; i < 4; i++) {
            rollList.add(random.nextInt(max - min + 1) + min);
        }

        return rollList;
    }

    int modifier(int input) {
        return (int) Math.floor((input - this.hp) / 2.0);
    }

    int getStrength() {
        return this.str;
    }

    int getDexterity() {
        return this.dxt;
    }

    int getConstitution() {
        return this.cnst;
    }

    int getIntelligence() {
        return this.intl ;
    }

    int getWisdom() {
        return this.wsdm;
    }

    int getCharisma() {
        return this.chrm;
    }

    int getHitpoints() {
        return this.hp + this.modifier(this.getConstitution());
    }
}
