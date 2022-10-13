import org.jfree.chart.ChartFactory;
import org.jfree.chart.ChartUtils;
import org.jfree.chart.JFreeChart;
import org.jfree.chart.plot.PlotOrientation;
import org.jfree.data.category.DefaultCategoryDataset;

import java.io.*;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;

public class Main {
    public static void main(String[] args) throws IOException {
        var data = DataReader.readData("D:\\Education\\teorver\\lab1\\Lab 1.2\\task_01_data\\input_10.txt");
        var listOfData = new ArrayList<Integer>();
        File output = new File("output.txt");
        var writerStream = new OutputStreamWriter(new PrintStream(output));
        for (var member : data.values()) {
            listOfData.add(member);
        }

        //FREQUENCY
        var frequencyTable = new HashMap<Integer, Integer>();
        for (var film: listOfData) {
            if (frequencyTable.containsKey(film))
                frequencyTable.put(film, frequencyTable.get(film)+1);
            else
                frequencyTable.put(film, 1);
        }
        System.out.println("FILM/Freq/Cum. fr.");
        writerStream.write("FILM/Freq/Cum. fr.");
        writerStream.write("\n");
        var cum = 0;
        for (var film: frequencyTable.keySet()) {
            cum+=frequencyTable.get(film);
            System.out.println(film + " / " + frequencyTable.get(film) + " / " + cum);
            writerStream.write(film + " / " + frequencyTable.get(film) + " / " + cum);
            writerStream.write("\n");
        }
        //END

        //MODA AND MEDIANA
        var moda = 0;
        var modaNumber = 0;
        for (var film:frequencyTable.keySet()) {
            if (frequencyTable.get(film) > moda)
            {
                moda = frequencyTable.get(film);
                modaNumber = film;
            }
        }

        var sorted = new ArrayList<Integer>(listOfData);
        Collections.sort(sorted);

        var mediana = 0;

        if (listOfData.size() % 2 == 0) { // медиана
            mediana = sorted.get(listOfData.size() / 2);
        } else {
            mediana = (sorted.get(listOfData.size() / 2) + sorted.get(listOfData.size() / 2)) / 2;
        }

        System.out.println("Moda is " + modaNumber);
        System.out.println("Mediana is " + mediana);
        writerStream.write("Moda is " + modaNumber);
        writerStream.write("\n");
        writerStream.write("Mediana is " + mediana);
        writerStream.write("\n");
        //END

        var total = 0;
        for (var number: listOfData) {
            total+=number;
        }
        var average = (double) total / listOfData.size();

        var strange_average = 0;
        for (var number : listOfData) {
            strange_average += Math.pow(number, 2);
        }
        strange_average = strange_average / listOfData.size();

        var dispersion = strange_average - Math.pow(average, 2);

        var av_sq_dis = Math.sqrt(dispersion);

        System.out.println(dispersion + " " + av_sq_dis);
        writerStream.write(dispersion + " " + av_sq_dis);

        final DefaultCategoryDataset dataset = new DefaultCategoryDataset();
        for (var film: frequencyTable.keySet()) {
            dataset.addValue(frequencyTable.get(film), film, film);
        }
        JFreeChart barChart = ChartFactory.createBarChart(
                "Film views statistic",
                "Films",
                "Frequency",
                dataset,
                PlotOrientation.VERTICAL,
                true, true, false);

        int width = 640; /* Width of the image */
        int height = 480; /* Height of the image */
        File barChart3D = new File( "barChart3D.jpeg" );

        ChartUtils chartUtils = new ChartUtils() {
            @Override
            public int hashCode() {
                return super.hashCode();
            }

            @Override
            public boolean equals(Object obj) {
                return super.equals(obj);
            }

            @Override
            protected Object clone() throws CloneNotSupportedException {
                return super.clone();
            }

            @Override
            public String toString() {
                return super.toString();
            }
        };
        writerStream.close();
        chartUtils.saveChartAsJPEG( barChart3D, barChart, width, height);
    }
}