from agents import build_search_agent , build_reader_agent,writer_chain,critic_chain

def run_research_pipeline(topic:str)->dict:

    state={}
    
    #SEARCH AGENT WORKING
    print("\n"+"="*50)
    print("Step 1 -Search agent is working...")
    print("="*50)

    search_agent=build_search_agent()
    search_result=search_agent.invoke({
        "messages":[("user",f"Find recent, reliable and detailed information about:{topic}")]
    })

    state["search_results"]= search_result['messages'][-1].content

    print("\n search result", state['search_results'])


     #READER AGENT WORKINGs
    print("\n"+"="*50)
    print("Step 2 -Reader agent is scraping top resources...")
    print("="*50)
    reader_agent=build_reader_agent()
    reader_result=reader_agent.invoke({
    "messages": [("user",
    f"Based on the following search results about '{topic}', "
    f"pick the most relevant URL and scrape it for deeper content. \n\n"
    f"Search Results:\n{state['search_results' ] [:800] }" 
       )]
     })
    
    state['scraped_content']=reader_result['messages'][-1].content
    print("\nScraped Content:",state['scraped_content'])
    
    #WRITER CHAIN
    print("\n"+"="*50)
    print("Step 3 -Writer chain is generating the research report...")  
    print("="*50)
    
    research_combined=(
        f"SEARCH RESULTS:\n{state['search_results']}\n\n"
        f"DETAILEDSCRAPED CONTENT:\n{state['scraped_content']} "

    )
    state["report"]=writer_chain.invoke(
        {
            "topic":topic,
            "research":research_combined
        }
    )

    print("\n Final Report\n",state['report'])

    #CRITIC REPORT
    print("\n"+"="*50)
    print("Step 4 -Critic chain is reviewing the research report...")
    print("="*50)
    state['feedback']=critic_chain.invoke({
        "report":state['report']
    })

    print("\n critic report\n", state['feedback'])

    return state

if __name__=="__main__":
    topic=input("\n Enter research topic :")
    run_research_pipeline(topic)

    



