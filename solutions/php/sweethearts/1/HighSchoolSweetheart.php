<?php

class HighSchoolSweetheart
{
    public function firstLetter(string $name): string
    {
        $name = trim($name);
        return $name[0];
    }

    public function initial(string $name): string
    {
        return strtoupper($this->firstLetter($name)) . ".";
    }

    public function initials(string $name): string
    {
        $str_arr = explode(" ", $name);
        $initials = "";

        foreach($str_arr as $element) 
        {
                $initials = $initials . $this->initial($element) . " ";
        }

        return trim( $initials);
    }

public function pair(string $sweetheart_a, string $sweetheart_b): string
{
    $s_heart_a = $this->initials($sweetheart_a);
    $s_heart_b = $this->initials($sweetheart_b);

return <<<HEART
     ******       ******
   **      **   **      **
 **         ** **         **
**            *            **
**                         **
**     $s_heart_a  +  $s_heart_b     **
 **                       **
   **                   **
     **               **
       **           **
         **       **
           **   **
             ***
              *
HEART;
}



        
}
