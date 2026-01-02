import java.util.List;
import java.util.Set;
import java.util.HashSet;

class GottaSnatchEmAll {

    static Set<String> newCollection(List<String> cards) {
        return new HashSet<>(cards);
    }

    static boolean addCard(String card, Set<String> collection) {
       return collection.add(card);
    }

    ////////////////
    
    static boolean canTrade(Set<String> myCollection, Set<String> theirCollection) {
        return containsCard(myCollection, theirCollection) && containsCard(theirCollection, myCollection);
    }

    private static boolean containsCard(Set<String> collection1, Set<String> collection2)  {
        for (var c : collection1) {
            if (!collection2.contains(c)) {
                return true;
            }
        }
        return false;
    }

    ////////////////


    static Set<String> commonCards(List<Set<String>> collections) {
        Set<String> commons = null; 
        for (var e : collections) {
            if (commons == null) {
                commons = new HashSet<>(e);
            }
            commons.retainAll(e);
        }
        return commons;
    }

    static Set<String> allCards(List<Set<String>> collections) {
        Set<String> commons = null; 
        for (var e : collections) {
            if (commons == null) {
                commons = new HashSet<>(e);
            }
            commons.addAll(e);
        }
        return commons;
    }
}
