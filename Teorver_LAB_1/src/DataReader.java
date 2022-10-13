import java.io.*;
import java.util.HashMap;
import java.util.Map;

public class DataReader {
    public static Map<Integer, Integer> readData(String path) throws IOException {
        var reader = new BufferedReader(new FileReader(new File(path)));
        var result = new HashMap<Integer, Integer>();
        var size = Integer.parseInt(reader.readLine());
        for (int a = 0; a< size; a++){
            result.put(a, Integer.parseInt(reader.readLine()));
        }
        return result;
    }
}
