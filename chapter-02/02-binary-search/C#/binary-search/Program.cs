// See https://aka.ms/new-console-template for more information

Console.WriteLine(binarySearch(new int[] {1, 23, 56, 87, 91, 101, 119, 137, 156, 178, 191}, 111));


string binarySearch(int[] array, int searchValue)
{
    int lowerBound = 0;
    int upperBound = array.Length - 1;
    while(lowerBound <= upperBound)
    {
        int middle = (lowerBound + upperBound) / 2;
        if (array[middle] == searchValue)
        {
            return $"Found {searchValue} at index {middle}";
        }
        else if (array[middle] < searchValue)
        {
            lowerBound = middle + 1;
        }
        else
        {
            upperBound = middle - 1;
        }
    }
    return $"Value {searchValue} not found in the array.";
}
