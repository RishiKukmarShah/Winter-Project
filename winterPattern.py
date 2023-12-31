'''
In this code, first a fuction called generate_winter_pattern is created which contains a nested for loops.
Finally the function is called by passing the value of rows and columns. Here randomly star is printed at the index.

*       *     *   *               * 
    *     *   *     *   * * *       
* * *         * * *   * * *         
* *   * * * *     *     *       *   
    * *     *   * * *   *       *   
*   * * *   *           * * *     * 
* *   *     *   *   * *       *     
              * * * * * * * * * *   
* *   * * *         * *       * *   
* * * *     *     *   * * * *   *   
*       * * * * *   *   * * *   * * 
      *   *     * *   *   *       * 
* * * *   *   *   *     *   *     * 
  *       * *   * *       * * *   * 
* * *   * * * *       *   * *   *  


'''


def generate_winter_pattern(rows, columns):
    for i in range(rows):
        for j in range(columns):
            if random.choice([True, False]):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print() # Move to the next line for the next row
        

            
generate_winter_pattern(15,18)
