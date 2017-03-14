import java.io.BufferedReader;
import java.io.FileReader;
import java.util.*;

import java.io.BufferedReader;
import java.io.FileReader;

public class ParseCSV {

  @SuppressWarnings("rawtypes")
  public static void main(String[] args) throws Exception {

  		ParseCSV parseObj=new ParseCSV();
  		String[] SingerList=parseObj.getsingers();

  	// 		for(int i=0;i<SingerList.length;i++){
			// System.out.println(i+" th singer "+SingerList[i]);
			// }

  		String[] GenreList=parseObj.getgenres(SingerList[0]);

  			for(int i=0;i<GenreList.length;i++){
			System.out.println(i+" th Genre "+GenreList[i]);
			}

  		String[] SongList=parseObj.getsongs(SingerList[0],GenreList);

  		  	for(int i=0;i<SongList.length;i++){
			System.out.println(i+" th song "+SongList[i]);
			}

		System.out.println("singer name "+SingerList[0]);
  		

  }

  @SuppressWarnings("rawtypes")
  public String[] getsingers() throws Exception {
  	HashSet<String> noDuplicate=new HashSet<String>();
		String splitBy = ",";
      	String line;
      	int count=0;
      	

      	
      		BufferedReader br = new BufferedReader(new FileReader("songs.csv"));

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
      	

      	
      		BufferedReader br = new BufferedReader(new FileReader("songs.csv"));

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
      	

      	
      		BufferedReader br = new BufferedReader(new FileReader("songs.csv"));

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