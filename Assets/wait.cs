using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class wait : MonoBehaviour
{

    public GameObject Figur = null;
    public GameObject Figur2 = null;


    public void Start()
    {
        Figur.SetActive(false);
        Figur2.SetActive(false);

        
        StartCoroutine(Waitfew());
    }


    private IEnumerator Waitfew()
    {
        

        yield return new WaitForSeconds(5);

        Figur.SetActive(true);
        Figur2.SetActive(true);
    }
}
