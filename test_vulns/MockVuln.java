/*
 MockVuln.java
 Safe-for-testing example class with patterns commonly flagged by static scanners.
 Do NOT use in production. Only commit to a disposable test repository.
*/

public class MockVuln {
    private static final String PASSWORD = "TEST_ONLY_DO_NOT_USE_PASSWORD_12345";
    public static String getPassword() { return PASSWORD; }

    public static String insecureMd5(String input) {
        try {
            java.security.MessageDigest md = java.security.MessageDigest.getInstance("MD5");
            byte[] digest = md.digest(input.getBytes("UTF-8"));
            StringBuilder sb = new StringBuilder();
            for (byte b : digest) sb.append(String.format("%02x", b));
            return sb.toString();
        } catch (Exception e) {
            return null;
        }
    }

    public static byte[] insecureAesEcb(byte[] key, byte[] plaintext) {
        try {
            javax.crypto.SecretKeySpec ks = new javax.crypto.SecretKeySpec(key, "AES");
            javax.crypto.Cipher cipher = javax.crypto.Cipher.getInstance("AES/ECB/PKCS5Padding");
            cipher.init(javax.crypto.Cipher.ENCRYPT_MODE, ks);
            return cipher.doFinal(plaintext);
        } catch (Exception e) {
            return null;
        }
    }

    public static void runShellCommand(String cmd) {
        try {
            Runtime.getRuntime().exec(new String[] { "/bin/sh", "-c", cmd });
        } catch (Exception e) {}
    }

    public static void main(String[] args) {
        System.out.println("MockVuln: static test artifact for security scanning only.");
    }
}
