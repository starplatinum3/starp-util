import java.util.HashSet;
import java.util.Set;

public class Test {

    String d="sto";
    Test(){
        d="3";
        // Constructor call must be the first statement in a constructorJava(1207959691)
        // super();
        // Class Object is the root of the class hierarchy. 
        // Every class has Object as a superclass.
        //  All objects, including arrays, 
        // implement the methods of this class.
    }
    public static void main(String[] args) {
        // String d="sto";
        // d.length()
        Set<Short> s = new HashSet<>();
        for(Short i=0;i<100;i++){
            s.add(i);
            s.remove(i-1);
            // Unlikely argument type int for remove(Object) on a Collection<Short>
        }
        System.out.println(s.size());
        // 100

       int res=  5+3+1+3+0+3;

       Object object=    new Object(){
        @Override
        public int hashCode() {
            // TODO Auto-generated method stub
            return 42;
        }
       };
       System.out.println(   object.hashCode());
    //    42
    
    }
}
