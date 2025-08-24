namespace targets {
// TODO: Insert the code for the alien class here
    class Alien {
    public:
        Alien(int x_coord, int y_coord){
            x_coordinate = x_coord;
            y_coordinate = y_coord;
        }
        int get_health(){
            return health;
        }
        bool hit(){
            if(is_alive()){
                health--;
                return true;
            }
            return false;
        }
        bool is_alive(){
            return health > 0;
        }
        bool teleport(int x_coord, int y_coord){
            x_coordinate = x_coord;
            y_coordinate = y_coord;
            return true;
        }
        bool collision_detection(Alien alien){
            return alien.x_coordinate ==  x_coordinate && alien.y_coordinate ==  y_coordinate;
        }
        
        int x_coordinate{0};
        int y_coordinate{0};
        int health{3};
};
    

}  // namespace targets