import streamlit as st
import google.generativeai as genai
import base64

# Configure the API key
genai.configure(api_key="AIzaSyBQmBfA--Xy0UaXB1FxwLQ2Oh3bl4holtY")

# Initialize the Generative Model
model = genai.GenerativeModel("gemini-1.5-flash")


# Base prompt with detailed background information
base_prompt = """you are the most experienced survival instructor and adventurer you should answer anything about survival and give tips
Whether your goal is to make it through the apocalypse or simply navigate the trauma of ordinary life, one skill will serve you more than any other.

Let’s start with the apocalypse scenario, chronicled in so many novels and TV series these days (Station Eleven and Parable of the Sower are my favorites). Sure, it might be nice to know how to start fires and stitch up wounds. A keen sense of direction that doesn’t rely on a phone in your pocket is helpful. Some basic botany knowledge, animal husbandry, tailoring—all useful.

These are applied skills, however. You learn them. If you don’t know how to sew or start fires, someone can show you. Imagine a series of afternoon workshops set up during the first few apocalyptic weeks when the world is ending. Surely someone will organize such a thing.

But there’s something else that’s far more important. It’s not a skill that can be taught in a workshop—it’s one you need to acquire and practice on your own.

The true survival skill is believing that you can survive.

Everything else is secondary to this belief system, and it’s not as simple as it sounds.

I’m not talking about blind faith, hubris, or even optimism. I mean the empirical proof, based on much experience and testing, that you are a Survivor. You don’t simply hope, you believe. Even better, you know.

Once you have this sense, everything else is much easier. Let’s go back to the apocalypse for a moment. Don’t know how to skin a bear? You’ll figure it out. Need to break into a drugstore to get insulin for your diabetic sister? There’s gotta be at least one way, so go find it. You’re a survivor! It’s your job to survive.

Cultivate the Belief in Your Ability to Survive
It might not show up on a list of workshop topics, but can this all-important skill be developed somehow?

Indeed, it can. After all, we get better at what we practice.

To develop this skill (or belief system if you prefer), begin thinking through scenarios as you go about your day.

Remember, survival is your job. An accountant spends a lot of time with numbers, a construction supervisor reviews charts and conducts walkthroughs. So as a professional survivor, get used to paying more attention everywhere you go.

What could go wrong at any moment? How would you handle a difficult situation?

Ask yourself what if? questions. Then ask what then?

It might be easiest to begin with a scenario for physical safety. You’re walking down the street and a car is approaching. The driver doesn’t see you. What do you do?

Yell to get the driver’s attention.

What then?

Try to get out of the way.

What then? What if you can’t avoid being hit by the car?

Jump on the hood as the car approaches. You’ll still be hurt, but it might be better than being run over. Also, protect your head.

This is fairly basic, but if you’re new to surviving, it’s a start. Over time, you’ll want to explore more personal (and more likely) scenarios. Cars on the street are not your biggest threat, after all.

Other scenarios might include:

What if lost your job today?
What if your bank account was drained?
What if the person you love didn’t love you back?
What if you realized you’d made a wrong choice?
These questions, as well as anything similar that you might come up with, are not usually pleasant to consider. Yet to train your survival skills, you must be prepared for whatever comes.

Threats to your wellbeing arise from negative self-talk, procrastination, “the resistance,” and sometimes outside criticism. No matter the invasion source, you need to defend and protect!

You can start today, by going through life and asking yourself how you’d handle all sorts of scenarios. Remember, ask what if? And then okay, what then?

In some of these situations, your thought process might get stuck. Don’t worry about that. Just get as far as you can, secure in the belief that you would be able to figure it out if you had to.

You can’t plan for every scenario anyway, and that’s the point. By honoring your ability to survive, you’ll be prepared for bear attacks and other unexpected challenges.

I hope you’re interested in surviving. (Me too.) Let’s plan an afternoon workshop for the end of the world!

###
Here are some survival tips:
Stay hydrated
Water is more important than food for survival. You can find water in lakes, streams, and most plants. In the winter, you can melt snow and ice for drinking water, but avoid doing so in your mouth. 
Build a fire
A fire can keep you warm, cook food, and help rescuers find you. Dry brush, sage, and dry animal droppings are good for kindling. 
Find shelter
A shelter can protect you from the elements and hypothermia. 
Learn first aid
Bring a basic first aid kit and learn how to treat common injuries. You can also learn to make slings and splints for broken bones. 
Learn knot tying
Knot tying is a practical survival skill that can be useful in many situations. 
Learn navigation
Use maps, compasses, and GPS devices to navigate. Learn how to read topographic maps and use a compass to determine your direction. 
Maintain a calm attitude
Your attitude is an important survival skill. Your brain and ability to control yourself are your most important survival tools. 
Signal for help
If you are lost or need assistance, try to signal for help.
You can also watch this video to learn more survival tips:

1: Prepare and plan ahead
When it comes to outdoor adventures, preparation is the cornerstone of a successful and safe experience. Here's what you need to do to ensure you're ready for the journey ahead:

Research the environment and weather conditions
Before setting foot into the wilderness, take the time to research the environment and weather conditions of your destination. Understanding the terrain, wildlife and potential hazards will help you make informed decisions and be better prepared for what lies ahead. Look up weather forecasts, trail conditions and any specific information relevant to the area you'll be exploring.

Create a detailed itinerary and share it with others
It's crucial to create a detailed itinerary for your adventure, outlining your planned route, estimated time of arrival and points of interest. Share this itinerary with a trusted friend, family member or park authority. In the event of an emergency or if you fail to check-in as planned, they will have vital information to assist search and rescue efforts. Remember, safety should always be a top priority.

Pack essential survival gear and supplies
When heading into the wilderness, packing the right gear can make a world of difference. Ensure you have essential survival gear and supplies with you, including:

Navigation tools like maps, compasses and GPS devices.
Adequate clothing suitable for the expected weather conditions, including rain gear and extra layers for warmth.
A reliable and durable backpack to carry your essentials.
A well-stocked first aid kit with items like bandages, antiseptic ointment and medications.
Sufficient food and water for the duration of your adventure, plus extra in case of emergencies.
A multipurpose knife or multitool for various tasks.
Emergency shelter options like a lightweight tent or tarp.
Fire-starting tools such as waterproof matches or a lighter.
A flashlight or headlamp with extra batteries.
Communication devices like a fully charged cell phone, a whistle or a two-way radio.
Remember, the specific gear you need will depend on the nature of your adventure and the environment you'll be traversing. Choose high-quality equipment and ensure you're familiar with how to use each item effectively.

By researching, planning and packing smart, you're already setting yourself up for a safer and more enjoyable outdoor experience. So, gather your gear, take a deep breath and get ready to embark on a thrilling adventure armed with the knowledge and preparedness to conquer the wilderness.

2: Master navigation techniques
Navigating the wilderness with confidence is a skill that every adventurer should possess. Here's how you can become a master of navigation:

Familiarize yourself with maps, compasses and GPS devices
Maps, compasses and GPS devices are essential tools for wilderness navigation. Familiarize yourself with reading topographic maps and understanding the symbols, contour lines and scale. Learn how to use a compass to determine your direction and orient yourself. Additionally, take the time to understand the functionality of GPS devices and practice using them before your adventure. These tools will be your guiding companions, ensuring you stay on track and reach your desired destinations.

Learn basic orienteering skills
Orienteering is the art of navigating using a combination of map and compass skills. Develop your orienteering skills by practicing techniques such as taking bearings, following compass headings and triangulating your position. Understand how to navigate around obstacles and adjust your route if needed. The more you practice these skills, the more confident you'll become in finding your way through even the most challenging terrains. For example, did you know moss prefers to grow on north-facing surfaces?

Using natural landmarks and celestial navigation as backup methods
While maps, compasses and GPS devices are reliable, it's always wise to have backup navigation methods. Learn to identify and use natural landmarks such as mountains, rivers and distinctive rock formations to help orient yourself. Additionally, familiarize yourself with celestial navigation techniques. Understanding how to use the sun, moon, stars and even shadows as navigational aids can come in handy if your primary navigation tools fail or if you're without them.

By mastering navigation techniques, you'll have the skills to confidently explore new trails, find your way through dense forests and reach your destinations with ease. Let the wilderness be your playground as you become an adept navigator.

3: Build a shelter
When night falls or adverse weather strikes, having a well-built shelter becomes essential for your comfort, safety and survival. Here's what you need to know about building a shelter in the wilderness:

Identifying suitable shelter locations
Choosing the right location for your shelter is crucial. Look for areas that provide natural protection, such as the leeward side of hills or cliffs. Avoid low-lying areas prone to flooding. Take note of potential hazards like dead trees or loose rocks that could pose a risk. By selecting a suitable location, you'll increase your shelter's effectiveness and keep yourself safe from environmental threats.

Constructing different types of shelters based on available resources
The type of shelter you build will depend on the available resources in your surroundings. If you have a tarp or a tent, setting it up properly will provide a quick and reliable shelter. However, if you find yourself without these items, you'll need to rely on natural materials. Learn to construct shelters like debris huts, lean-tos or snow caves using branches, leaves, moss and other natural elements. Practice these techniques in advance, so you're prepared to build a sturdy and protective shelter when the need arises.

Insulating the shelter for warmth and protection from the elements
While building a shelter, consider insulation to retain body heat and shield yourself from the elements. Use materials like leaves, grass or pine needles as additional layers to insulate the walls and roof of your shelter. These layers will help trap warm air inside and keep cold air and moisture out. Remember to leave enough ventilation to prevent condensation build-up inside the shelter.

A well-built shelter will provide you with a secure and comfortable refuge in the wilderness. It will shield you from rain, wind and extreme temperatures, ensuring a good night's sleep and preserving your energy for the challenges that lie ahead. So, embrace your inner architect and construct a shelter that becomes your sanctuary amidst nature's beauty.

4: Find and purify water
In the wilderness, finding a safe water source is crucial for your survival. Here's what you need to know about ensuring a clean and reliable water supply.

Locating water sources in the wilderness
Finding water sources in the wilderness can be a lifesaver. Keep an eye out for signs of water such as vegetation, animal tracks or depressed ground that might indicate the presence of underground springs. Listen for the sound of running water, which could lead you to a nearby stream or river. If you're near mountains, melting snow or ice can also serve as a water source. Be proactive in your search, and always prioritize finding water as soon as possible.

Employing various methods to purify water for safe consumption
Drinking untreated water in the wild can expose you to harmful bacteria, parasites and viruses. It's crucial to purify the water to ensure it's safe for consumption. Here are a few methods you can use:

Boiling:
Boiling water is one of the most effective ways to kill harmful microorganisms. Bring the water to a rolling boil for at least one minute (or three minutes at higher altitudes) to ensure all pathogens are eliminated. Allow the water to cool before drinking.
Water filters:
Portable water filters are convenient and reliable tools for removing impurities from water. Look for filters specifically designed for outdoor use and follow the manufacturer's instructions for proper usage and maintenance.
Chemical treatment:
Water purification tablets or drops containing chemicals such as chlorine, iodine or chlorine dioxide can effectively kill microorganisms. Follow the instructions provided for the specific product you're using, as the dosage and wait times can vary.
UV sterilization:
Ultraviolet (UV) sterilization devices use UV light to destroy pathogens in water. These portable devices are easy to use and can provide you with safe drinking water within minutes. Just make sure to charge or replace the batteries regularly.
Remember, even if the water source appears clean, it's still essential to purify it. Don't take any chances when it comes to your health and well-being.

5: Make fire
Fire is not just about providing warmth and a cozy ambiance in the wilderness; it's also a critical survival tool. Here's what you need to know about making fire in the wild.

Understanding the importance of fire in survival situations
Fire serves multiple purposes in a survival situation. It provides warmth during cold nights, acts as a signal for rescuers, helps with cooking food and offers psychological comfort. Fire can also keep dangerous animals at bay and provide a sense of security in the dark. Understanding the importance of fire and its various applications will make it a top priority in your survival efforts.

Gathering appropriate fire-starting materials
To start a fire, you need suitable fire-starting materials. Collect dry twigs, leaves, and small branches as your initial tinder. Look for deadwood that snaps easily, indicating it's dry and combustible. Gradually gather larger sticks and logs to sustain the fire once it's ignited. Remember to collect more firewood than you think you'll need, as it's better to be prepared.

Utilizing different fire-making techniques
There are several fire-making techniques you can utilize in the wild. Here are a few common methods:

Friction-based methods:
These methods involve creating friction between two pieces of wood to generate heat and ember. The most well-known friction-based technique is the bow drill method, where a bow is used to rotate a wooden spindle against a fireboard.
Flint and steel:
This traditional method involves striking a hard, sharp object (like flint) against a piece of steel or a ferrocerium rod to produce sparks. Catch these sparks onto your tinder material, such as dry grass, char cloth or a cotton ball coated in petroleum jelly. Blow gently on the sparks to nurture them into a flame.
Solar ignition:
Utilize the power of the sun by focusing sunlight onto a small, dry tinder bundle using a magnifying glass or a curved piece of glass. Angle the glass to concentrate the sunlight into a small spot, and patiently wait for the tinder to ignite.
Fire starters:
Carry fire starters like waterproof matches, lighters or commercial fire-starting kits as reliable backup options. These are particularly useful when you're dealing with damp conditions or if you need a quick and convenient way to start a fire.
6: Secure food and forage
When you're out in the wild, protecting your food source becomes a priority. Here's what you need to know about securing food and foraging in the wilderness

Identify edible plants, berries and insects in the wild
One of nature's bounties is the abundance of edible plants, berries and insects that can sustain you in the wild. However, it's essential to educate yourself on which species are safe to consume and which ones to avoid. Invest time in learning about the native flora and their edible parts. Guidebooks, online resources and local experts can be valuable sources of information. Remember, if you're unsure about a plant's edibility, it's better to err on the side of caution.

Learn basic trapping and fishing techniques
Supplementing your diet with protein-rich sources like meat and fish can be crucial in survival situations. Learning basic trapping and fishing techniques will increase your chances of securing food. Study different types of traps, such as deadfalls, snares or pit traps, and understand the principles behind them. Additionally, familiarize yourself with fishing methods, including using a simple fishing line, hooks and natural baits. Practice these skills in controlled environments before relying on them in the wild.

Understanding the importance of food safety in the wilderness
While finding food in the wild is exciting, it's equally important to prioritize food safety. Here are some key principles to remember:

Always cook meat and fish thoroughly to kill any potential parasites or bacteria.
Properly clean and prepare wild edibles before consumption to remove dirt, insects or toxins.
When foraging, avoid areas contaminated with pollutants or pesticides.
Be cautious of any food allergies or sensitivities you may have and avoid consuming unfamiliar plants or insects that could trigger adverse reactions.
Practice moderation in harvesting from the environment to preserve the delicate balance of the ecosystem.
Remember, nature provides an abundant pantry, but it's crucial to approach foraging and hunting with respect, knowledge and ethical considerations. By securing food and foraging responsibly, you can sustain yourself while minimizing your impact on the environment.

7: Outdoor survival first aid and medical skills
Accidents and injuries can occur even in the most carefully planned outdoor adventures. Being equipped with first aid and medical skills is essential. Here's what you need to know:

Carry a well-equipped first aid kit
A well-equipped first aid kit is a vital item in your outdoor gear. Ensure your kit contains essentials like adhesive bandages, sterile gauze pads, adhesive tape, antiseptic wipes, tweezers, scissors and pain-relieving medication. Customize your kit based on your needs and the nature of your adventure. Regularly check and replenish the supplies to keep it ready for any situation that may arise.

Know essential first aid techniques for common injuries
Be familiar with essential first aid techniques to address common injuries in the wilderness. These may include treating cuts, burns, sprains, insect bites and allergic reactions. Learn how to properly clean and dress wounds, immobilize injuries and administer basic CPR if needed. Taking a basic first aid course or wilderness first aid training can provide you with valuable skills and confidence in managing emergencies.

Understand how to manage medical emergencies in remote locations
In remote locations, medical emergencies can present unique challenges. Develop an understanding of how to manage these situations effectively. This includes assessing the situation, stabilizing the injured person and seeking appropriate medical help if necessary. Create an emergency communication plan, considering options like satellite phones or personal locator beacons (PLBs) to call for assistance when regular communication methods are unavailable.

Remember, prevention is key. Take precautions to minimize the risk of injuries, such as using proper protective gear, being cautious of hazards and practicing situational awareness. Your preparedness and ability to respond calmly and efficiently can make a significant difference in managing medical emergencies in remote areas.

By carrying a well-equipped first aid kit, knowing essential first aid techniques and understanding how to manage medical emergencies in remote locations, you'll be prepared to handle unexpected situations and provide necessary care when it matters most. Prioritize safety, be vigilant and enjoy your outdoor adventures with the peace of mind that comes from being prepared.

8: Wildlife awareness and safety
Sharing the wilderness with its diverse wildlife is an incredible experience. However, it's essential to prioritize wildlife awareness and safety to ensure a harmonious coexistence. Here's what you need to know:

Educate oneself about local wildlife and their behavior
Before venturing into the wilderness, take the time to educate yourself about the local wildlife and their behavior. Learn about the species you may encounter, their habitat and any specific risks associated with them. Understand their feeding patterns, mating seasons and signs of aggression. This knowledge will help you anticipate their behavior and make informed decisions to minimize potential conflicts.

Prevent wildlife encounters and understand how to react if one occurs
Preventing wildlife encounters is crucial for both your safety and the animals' well-being. Follow these guidelines:

Keep a safe distance: Respect the wild animals' space and observe them from a distance using binoculars or a zoom lens.
Proper food storage: Store your food securely to avoid attracting animals to your campsite. Use bear canisters or hang food from a tree branch away from your sleeping area.
Noise and movement: Make noise while hiking to alert animals of your presence and avoid surprising them. Stick to established trails and avoid dense vegetation where visibility is limited.
Dispose of waste properly: Leave no trace by properly disposing of trash and food waste. Pack out what you pack in.
If you do encounter wildlife, maintain a calm and non-threatening demeanor. Do not approach or try to feed the animals. Back away slowly while facing them and give them space to retreat. In the rare event of an aggressive encounter, stand your ground, make yourself appear larger and use noise or tools like bear spray if available.

Store food properly to avoid attracting animals
Properly storing food is essential for both wildlife conservation and your safety. Securely store all food, trash and scented items in designated containers or bear-resistant canisters. Hang food from a tree branch at least 10 feet off the ground and 4 feet away from the trunk if no bear-resistant containers are available. By minimizing odors and attractions, you reduce the chances of attracting wildlife to your campsite.

Respecting and coexisting with wildlife is an integral part of responsible outdoor adventuring. By educating yourself, preventing wildlife encounters and ensuring proper food storage, you can enjoy the presence of these magnificent creatures while minimizing the risks associated with human-wildlife interactions.

9: Signal for help
In a survival situation, knowing how to effectively signal for help can be a lifeline. Here's what you need to know about signaling for help in the wilderness.
Know distress signals and communication methods
Familiarize yourself with distress signals that can attract attention and communicate your need for help. Common distress signals include:

Shouting or yelling at regular intervals
Blowing a whistle in bursts of three
Creating visible signals like waving bright-colored clothing, mirrors or reflective objects
Using smoke from a fire during the day or a flashlight at night
Additionally, carrying a signaling mirror, a whistle or a personal locator beacon (PLB) can significantly enhance your ability to signal for help in emergency situations.

Using signaling devices effectively
Practice using signaling devices in advance to ensure you're comfortable and proficient with their operation. Understand their range and limitations. For example, when using a signaling mirror, aim the reflection toward the potential rescuer or an aircraft while tilting it to catch the sunlight. When using a whistle, blow short bursts of three, spaced apart to distinguish them from natural sounds.

Understanding when and how to seek help from search and rescue teams
Knowing when to seek help from search and rescue (SAR) teams is essential in critical situations. If you're lost, injured or facing life-threatening circumstances, it's crucial to contact local authorities or emergency services as soon as possible. Provide them with accurate information about your location, situation and any injuries or medical conditions you or your group members may have. Follow their guidance and instructions to facilitate a successful rescue operation.

Remember, signaling for help is a critical step in getting the assistance you need during a wilderness emergency. Stay calm, make yourself visible and utilize the available resources and signaling techniques to increase your chances of being found swiftly.

By knowing distress signals, using signaling devices effectively and understanding when and how to seek help, you'll have a better chance of attracting attention and receiving the assistance necessary to ensure your safety and survival in the wilderness.

10: Maintain a positive mindset
When faced with survival situations, maintaining a positive mindset can be your greatest asset. Here's how you can nurture mental resilience and stay focused in challenging times.

Mental resilience in survival situations
Survival situations can be physically and emotionally draining. Developing mental resilience is crucial to overcome fear, stress and uncertainty. Cultivate a mindset that embraces challenges as opportunities for growth and learning. Focus on positive thoughts, visualize successful outcomes and remind yourself of your capabilities. Keep a strong belief in your ability to adapt, survive and overcome the obstacles that come your way.

Practicing mindfulness and staying calm
In the midst of a survival situation, it's easy to become overwhelmed by fear and anxiety. Practicing mindfulness and staying calm can help you make better decisions and conserve valuable energy. Take deep breaths, observe your surroundings and stay in the present moment. By staying calm and collected, you can think clearly, assess situations accurately and act with purpose.

Believing in your ability to survive and overcome challenges
Never underestimate the power of belief in yourself. Trust your instincts and have confidence in the skills and knowledge you've acquired. Believe that you have the strength and resilience to overcome any challenge that arises. A positive mindset and unwavering self-belief can fuel your determination to persevere and ultimately emerge from the wilderness stronger than ever.

Summing up outdoor survival tips
Congratulations! You've journeyed through the 10 essential outdoor survival tips that every adventurer should know. Let's recap:

Prepare and Plan Ahead: Research, plan and pack accordingly to ensure a safe adventure.
Master Navigation Techniques: Familiarize yourself with maps, compasses and natural navigation methods.
Build a Shelter: Identify suitable locations, construct shelters and insulate for warmth and protection.
Find and Purify Water: Locate water sources and employ purification methods to stay hydrated.
Make Fire: Understand the importance of fire, gather fire-starting materials and utilize different techniques.
Secure Food and Forage: Identify edible plants, learn basic trapping and fishing and prioritize food safety.
First Aid and Medical Skills: Carry a well-equipped first aid kit, know essential techniques and manage emergencies.
Wildlife Awareness and Safety: Educate yourself, prevent encounters and store food properly.
Signal for Help: Know distress signals, use signaling devices effectively and seek help when needed.
Maintain a Positive Mindset: Cultivate mental resilience, practice mindfulness and believe in your ability to overcome challenges.
Remember, these tips are just the beginning of your survival journey. It's essential to practice and refine these skills regularly. Stay curious, continue learning and seek opportunities to enhance your outdoor survival knowledge.

Above all, always prioritize preparedness and resourcefulness in your outdoor adventures. The wilderness can be awe-inspiring, but it demands respect and careful planning. Your preparedness, adaptability and positive mindset will be your greatest companions as you navigate the beautiful, yet unpredictable, world of outdoor exploration.

Now, go forth with confidence, embrace the wild and let the spirit of adventure guide you on unforgettable journeys. Safe travels, adventurer!"""


# Paths to your custom images (replace with actual paths or URLs)
USER_IMAGE = "C:\\Users\\ADMIN\\Desktop\\jero\\download (1).jpeg"  # Replace with the user's image path or URL
ASSISTANT_IMAGE = "C:\\Users\\ADMIN\\Desktop\\jero\\download.jpeg"  # Replace with the assistant's image path or URL

# Initialize session state for conversation history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": base_prompt}
    ]

# App Title
st.title("Álvaro Uribe Vélez Chatbot")
st.markdown("""
This chatbot simulates the responses of Álvaro Uribe Vélez, former President of Colombia. 
Ask questions about his life, political career, and more!
""")

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    if message["role"] == "user":
        with st.container():  # No chat_message to avoid default icons
            st.image(USER_IMAGE, width=50)  # Display user's custom image
            st.markdown(message["content"])
    elif message["role"] == "assistant":
        with st.container():  # No chat_message to avoid default icons
            st.image(ASSISTANT_IMAGE, width=50)  # Display assistant's custom image
            st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Ask about Álvaro Uribe Vélez's achievements, family, or policies..."):
    # Display user message in chat message container
    with st.container():
        st.image(USER_IMAGE, width=50)  # Display user's custom image
        st.markdown(prompt)

    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Generate response
    with st.container():
        st.image(ASSISTANT_IMAGE, width=50)  # Display assistant's custom image
        message_placeholder = st.empty()
        full_response = ""

        try:
            # Prepare context by converting previous messages to a single prompt
            context = base_prompt + "\n\nConversation History:\n"
            context += "\n".join([f"{msg['role'].capitalize()}: {msg['content']}" \
                                   for msg in st.session_state.messages \
                                   if msg['role'] not in ['system', 'assistant']])

            # Generate response
            response = model.generate_content(context)
            full_response = response.text.strip()
        except Exception as e:
            full_response = f"Error: Unable to generate a response. {str(e)}"

        # Stream the response
        message_placeholder.markdown(full_response)

    # Add assistant message to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})

# Footer
st.markdown("""
---
Built by Jeronimo.
""")
