read -r W H
# N: maximum number of turns before game over.
read -r N
read -r X0 Y0
lowestX=0
lowestY=0
highestX="$W"
highestY="$H"

# game loop
while true; do
    read -r bombDir

    case "${bombDir:0:1}" in
        "D") lowestY=$(($Y0 + 1));;
        "U") highestY=$(($Y0 - 1));;
        "L") highestX=$(($X0 - 1));;
        "R") lowestX=$(($X0 + 1));;
    esac    
    case "${bombDir:1:1}" in 
        "L") highestX=$(($X0 - 1));;
        "R") lowestX=$(($X0 + 1));;
    esac

    X0=$((($highestX + $lowestX) / 2));
    Y0=$((($highestY + $lowestY) / 2));

    echo "$X0 $Y0";

done
