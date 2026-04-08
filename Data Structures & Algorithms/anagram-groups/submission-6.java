class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();

        for (String word : strs) {
            char[] ch = word.toCharArray();
            Arrays.sort(ch);
            String key = new String(ch);
            if (map.containsKey(key)) {
                map.get(key).add(word);
            }
            else {
                List<String> newList = new ArrayList<>();
                newList.add(word);
                map.put(key, newList);
            }
        }
        return new ArrayList<>(map.values());
    }
}
