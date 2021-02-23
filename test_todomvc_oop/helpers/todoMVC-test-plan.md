[Github](https://github.com/fkthereality/codarium/blob/ToDoMVC/todoMVC-test-plan.md)
### A priority ###
     ( hight ) high priority
     ( medium ) medium priority
     ( low ) low priority
     ( lowest ) You can forget about this item

### Functional map ###
* **TodoMVC save data in storage after restart functionality**

* **Operations for ALL**
    - ( hight ) Create 
    - Edit 
      - undo all changes:    
          -  ( hight ) Escape 
      - confirm all changes:
          -  ( hight ) Enter      
          -  ( low ) Tab
          -  ( low ) Click outside of editing form           
          -  ( lowest ) Control+Enter

    - Complete 
      - ( hight ) one 
      - ( low ) All

    - Activate  
      - ( hight ) one 
      - ( low ) All

    - Delete 
       - ( hight ) X 
       - ( lowest ) Clear Completed
       - ( lowest ) Edit to blank

* **Operations on the Active and Completed**
       - same where appropriate with correspondingly lower priorities (details skipped for now)

**Note: Clear completed button, items left counter and filters are not required according to the terms of reference**
* **( low ) Items left counter in each of filters separately**
  
    - decrement
    - unchange
    - increment

* **( lowest ) Button Clear completed**
    - is visible when  1 or more todos completed
    - is hidden when no completed todos
    
* **( low ) Filters**
    - All
    - Active
    - Completed  
  
  
### Scenario: 'TodoMVC - basic functionality' ###

* Open https://todomvc4tasj.herokuapp.com/

   * create 'a', 'b'
     + `assert list: 'a', 'b'`
     
   * edit 'a' to 'a edited'
   * cancel edit 'a edited' to 'a to be canceled' 
     + `assert list: 'a edited' ,  'b'`
     
  * complete 'a edited'
  * Clear Complited 
      + `assert list: 'b'`
      
  * delete 'b'
       + `assert list: empty` 
