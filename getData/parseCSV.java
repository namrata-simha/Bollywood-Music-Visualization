/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package getData;

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.HashSet;

/**
 *
 * @author Namrata Simha
 */
public class parseCSV {
    String path = "C:\\Users\\namra\\Desktop\\Study Material\\Master Of Science (M.S.) Computer Science\\2. Winter 2017\\CMPS 263\\Project\\BollywoodViz\\songs.csv";
      @SuppressWarnings("rawtypes")
  public String[] getsingers() throws Exception {
  	HashSet<String> noDuplicate=new HashSet<String>();
		String splitBy = ",";
      	String line;
      	int count=0;
      	     	
      		BufferedReader br = new BufferedReader(new FileReader(path));

      		while((line = br.readLine()) != null){
        		String[] b = line.split(splitBy);
        		if(!b[3].equals("NotFound")){
        			//System.out.println(b[3] + " singer name");
        			noDuplicate.add(b[3]);
	        	}
      		}
      		
 
			//System.out.println(noDuplicate.size()+" noDuplicate.size()");

			String[] noDupArray = new String[noDuplicate.size()];
			noDuplicate.toArray(noDupArray);
			//System.out.println(noDupArray.length+" noDupArray length after");
			br.close();
			
      		return noDupArray;
  }


  @SuppressWarnings("rawtypes")
  public String[] getgenres(String singer_name) throws Exception {
  	HashSet<String> noDuplicate=new HashSet<String>();
		String splitBy = ",";
      	String line;
      	int count=0;
      	

      	
      		BufferedReader br = new BufferedReader(new FileReader(path));

      		while((line = br.readLine()) != null){
        		String[] b = line.split(splitBy);
        		if(b[3].equals(singer_name)){
        			//System.out.println(b[3] + " singer name");
        			noDuplicate.add(b[0]);
	        	}
      		}
      		
 
			//System.out.println(noDuplicate.size()+" noDuplicate.size()");

			String[] noDupArray = new String[noDuplicate.size()];
			noDuplicate.toArray(noDupArray);
			//System.out.println(noDupArray.length+" noDupArray length after");
			br.close();
			
      		return noDupArray;
  }


  @SuppressWarnings("rawtypes")
  public String[] getsongs(String singer_name,String[] GenreList) throws Exception {
  	HashSet<String> noDuplicate=new HashSet<String>();
		String splitBy = ",";
      	String line;
      	int count=0;
      	   	
      		BufferedReader br = new BufferedReader(new FileReader(path));

      		while((line = br.readLine()) != null){
      			for(int i=0;i<GenreList.length;i++){
        			String[] b = line.split(splitBy);
        			if(b[3].equals(singer_name) && b[0].equals(GenreList[i])){
        			//System.out.println(b[3] + " singer name");
        				noDuplicate.add(b[1]);
        			}
	        	}
      		}
      		
			//System.out.println(noDuplicate.size()+" noDuplicate.size()");

			String[] noDupArray = new String[noDuplicate.size()];
			noDuplicate.toArray(noDupArray);
			//System.out.println(noDupArray.length+" noDupArray length after");
			br.close();
			
      		return noDupArray;
  }
}
