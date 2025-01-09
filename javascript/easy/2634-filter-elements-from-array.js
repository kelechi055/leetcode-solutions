/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    filteredArr = []; // Make an empty array to store the filtered elements - O(1)

    for(let i = 0; i < arr.length; i++){ // Iterate through every element in arr - O(n)
        fn(arr[i], i); // Do the fn function on the specific element in index i - O(1)
        if(fn(arr[i], i)) { // If the fn'ed element is true, add the element to filteredArr - O(1)
            filteredArr.push(arr[i]); 
        }
    }
    return filteredArr;
    // Time Complexity: O(n)
};
