/*eslint-disable*/
export default function hasValuesFromArray(set, array) {
	const allElementsinSet = array.every(element => set.has(element));

	return allElementsinSet;
}
