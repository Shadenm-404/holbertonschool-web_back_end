export default function appendToEachArrayValue(array, appendString) {
  for (const index of array.keys()) {
    array[index] = appendString + array[index];
  }

  return array;
}
