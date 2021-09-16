#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int main()
{
    /* W = building width, H = building height, N = game turns
        X0 = batman x position, Y0 = batman y position   */
    int W, H, N, X0, Y0;
    scanf("%d%d%d%d%d", &W, &H, &N, &X0, &Y0);  

    int lowest_y, lowest_x, highest_y, highest_x;
    lowest_y = 0; lowest_x = 0; highest_y = H; highest_x = W;

    // game loop
    while (1) {
        char bomb_dir[4];
        scanf("%s", bomb_dir);

        switch(bomb_dir[0]) {
            case 'D' : lowest_y = Y0 + 1;
                break;      
            case 'U' : highest_y = Y0 - 1;
                break;
            case 'L' : highest_x = X0 - 1;
                break;
            case 'R' : lowest_x = X0 + 1;
                break;
        }
        switch(bomb_dir[1]) {
            case 'L' : highest_x = X0 - 1;
                break;
            case 'R' : lowest_x = X0 + 1;
                break;
        }

        Y0 = (highest_y + lowest_y) / 2;
        X0 = (highest_x + lowest_x) / 2;

        printf("%i %i\n", X0, Y0);
    }

    return 0;
}
