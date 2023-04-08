public class CClass {
    static class B {
        class C {

        }

    }

    public static void main(String[] args) {
        CClass.B.C c = new CClass.B.C();
    }
    // pub
    // main(String[] args)
    // {
    // A.B.C c = new A.B.C();
    // }

}
