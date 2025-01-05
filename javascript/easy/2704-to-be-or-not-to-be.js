/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    return{
        toBe: function(otherVal){ 
            if(val === otherVal){ //if two values are thesame, return true: O(1)
                return true;
            }
            if(val !== otherVal){ // if two values are not thesame, throw "Not Equal" O(1)
                throw ("Not Equal");
            } else{ // for edge cases like the other value being null, throw a "Not Equal" error O(1)
                throw error ("Not Equal");
            }
        },

        notToBe: function(otherVal){
            if(val !== otherVal){ //if two values are not thesame, return true: O(1)
                return true;
            }
            if(val === otherVal){ // if two values are thesame, throw "Equal" O(1)
                throw ("Equal");
            } else {
                throw error ("Equal"); // for edge cases like the one value being null, throw a "Equal" error O(1)
            }
        }
    }
};

// Time Complexity: O(1)

/**
 * expect(5).toBe(5); // 5 === 5, so this returns true
 * expect(5).notToBe(5); // 5 === 5, so this throws "Equal"
 * expect(5).notToBe(null); // 5 is !== null, so this returns true
 */