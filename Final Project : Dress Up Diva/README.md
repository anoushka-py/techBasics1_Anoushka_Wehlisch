# Dress Up Diva

<p><img width="350" height="270" alt="image" src="https://github.com/user-attachments/assets/8938424c-2e0a-4ba6-9918-b0a860721a65" /> <img width="360" height="270" alt="image" src="https://github.com/user-attachments/assets/6c3f21f3-b474-438b-9f52-d3e745eec834" />
</p>




Dress Up Diva is a dress up game built in Python with Pygame. The player dresses a custom-drawn character through an interactive closet, then watches a final "runway" reveal of the outfit they created.

## How to Run the Game

Requirements : 
- Python 3.12 (or similar recent version)
- Pygame - only external library used (window, drawing, images, fonts, input, game loop)
- Other imports used : sys (cleanly exiting the program), random (random sparkle position/size/speed/direction), math (trigonometry for sparkle burst)

## Project History

### Outfit Options

<table>
<tr>
<td align="center"><b>Hair</b></td>
<td><img src="Assets/Hair/Hair%201.PNG" width="120"></td>
<td><img src="Assets/Hair/Hair%202.PNG" width="120"></td>
<td><img src="Assets/Hair/Hair%203.PNG" width="120"></td>
<td><img src="Assets/Hair/Hair%204.PNG" width="120"></td>
<td><img src="Assets/Hair/Hair%205.PNG" width="120"></td>
</tr>
<tr>
<td align="center"><b>Tops</b></td>
<td><img src="Assets/Tops/Top%201.PNG" width="120"></td>
<td><img src="Assets/Tops/Top%202.PNG" width="120"></td>
<td><img src="Assets/Tops/Top%203.PNG" width="120"></td>
<td><img src="Assets/Tops/Top%204.PNG" width="120"></td>
<td><img src="Assets/Tops/Top%205.PNG" width="120"></td>
</tr>
<tr>
<td align="center"><b>Bottoms</b></td>
<td><img src="Assets/Bottoms/Bottom%201.PNG" width="120"></td>
<td><img src="Assets/Bottoms/Bottom%202.PNG" width="120"></td>
<td><img src="Assets/Bottoms/Bottom%203.PNG" width="120"></td>
<td><img src="Assets/Bottoms/Bottom%204.PNG" width="120"></td>
<td><img src="Assets/Bottoms/Bottom%205.PNG" width="120"></td>
</tr>
<tr>
<td align="center"><b>Shoes</b></td>
<td><img src="Assets/Shoes/Shoes%201.PNG" width="120"></td>
<td><img src="Assets/Shoes/Shoes%202.PNG" width="120"></td>
<td><img src="Assets/Shoes/Shoes%203.PNG" width="120"></td>
<td><img src="Assets/Shoes/Shoes%204.PNG" width="120"></td>
<td><img src="Assets/Shoes/Shoes%205.PNG" width="120"></td>
</tr>
  
<tr>
<td align="center"><b>Accessories</b></td>
<td><img src="Assets/Accessories/Accessory%201.PNG" width="120"></td>
<td><img src="Assets/Accessories/Accessory%202.PNG" width="120"></td>
</tr>
</table>

Before I was able to start coding my fashion game, I had to create all of the clothing, hair, and accessory options for my character. The character (or “diva”) to dress up was also drawn entirely by me. I used a program called “Pixquare” on my iPad to single-handedly draw every single pixel that would eventually create the character for my game. After that, I had to draw all of the clothes by hand too. I had to be very careful to align the pixels with the base character so I wouldn’t mess up the proportions.

I originally had the ambition to add different skin tones, but even drawing one character proved to be challenging and time-consuming enough. I would have liked to add more variety to my options, but ultimately decided it would be better to work with what I had created and move on.

This project was built incrementally, one feature at a time. Below is the rough order it came together in.

**1. Title Screen**
- Set up the Pygame window and caption.
- Built the "DRESS UP DIVA" title and a "PLAY" button using basic rectangles
and centered text.
- Grouped all colors/fonts into a "design settings" section at the top, so the look
could be changed later without touching the logic.
- Added a hover-color swap and a scale-up effect on the button.

**2. Fade Transition + Character Placement**
- Introduced game_state , a simple text variable used as a "state machine" to
track which screen is active ( "title" vs "game" ).
- Built a fade-to-black-and-back transition using a rising/falling fade_alpha
value (0–255) drawn as a semi-transparent overlay.
- Loaded and scaled the hand-drawn character PNG, positioning her on the left
side of the screen.

**3. Closet HUD (Visual Only)**
- Built a rounded panel on the right, split into 4 equal sections (hair / top / bottom
/ shoes).
- Represented each section as a dictionary inside a list ( closet_slots ), the
same "list of dictionaries" pattern taught in class.
- Added white separator lines and triangle arrow shapes for cycling through
options.
- Restyled colors/border to match a hand-drawn reference image (pink + gold
theme).

**4. Clothing Dictionaries + Equipping System**
- Created one list of dictionaries per clothing category ( hair_options ,
top_options , bottom_options , shoe_options , accessory_options ), each
entry holding a name and image file path.
- Wrote a load_clothing_images() function that loads each image once and
produces both a full-size version (for equipping) and a cropped thumbnail (for
previewing in the closet).
- Connected everything with two dictionaries: category_options (links
category names to their option lists) and equipped_items (tracks what's
currently worn per category).
- Wired up the arrows to cycle through options and clicking an item to equip it,
with DRAW_ORDER controlling stacking order (e.g. hair always drawn on top of
tops).

**5. Popup, Outfit Completion, and Accessories**
- Added an intro message bubble ("This diva is in dire need of a makeover…")
with branching dialogue options.
- Added a completion check ( outfit_complete ) that unlocks a "DONE" button
once all 4 categories are filled. 
- On "DONE": grew the character and her clothes, slid her to the center of the
screen, and faded out the closet
- Added a second popup ("Wait, what about accessories?") that opens a 2-section
accessory closet, reusing the same list-of-dictionaries pattern.

**6. Final Transition Sequence**
- Built a 3-stage "camera pan" showing off the finished outfit: zooming into the
character and sliding her sideways so different parts of her body pass through
the screen's center.
- Added a full-body "reveal" pose at the end, along with a sparkle burst effect
(using random and math.cos / math.sin to send sparkles flying outward).
- Finished with a closing "Thank you for helping this diva!" message.

## File Structure 

Header comment (1-5)<br>
Imports (7-10)<br>
Setup (lines 13-18)<br>
Design Settings (20-38<br>
Fonts (lines 40-53)<br>
Text Shadow (55-63)<br>
Title Text (65-68)<br>
Play Button (70-77)<br>
Character Artwork (79-90)<br>
Background Images (92-99)<br>
Closet Layout (101-130)<br>
Accessory Closet (131-148)<br>
Clothing Options (l150-187)<br>
Clothing Loading (189-215)<br>
Clothing Dictionaries (217-235)<br>
Intro Pop Up (237-269)<br>
Outfit Finalization (271-292)<br>
Accessory Prompt (294-300)<br>
Done Button 2 (302-305)<br>
Screen Transition (308-315)<br>
Final Transition (317-353)<br>
Main Loop (355-945) <br>
Shutdown (944-945)

## Assets 

Assets/<br>
├── character_base.png<br>
├── backgrounds/<br>
│ ├── title_background.jpeg<br>
│ └── game_background.jpeg<br>
├── Hair/<br>
├── Tops/<br>
├── Bottoms/<br>
├── Shoes/<br>
└── Accessories/

## Use of AI

- Initial architecture guidance (i.e explaining title screen -> dress-up screen -> ending sequence)
- Pygame command tutoring (explainig simple core functions, i.e pygame.Rect, pygame.transform.smoothscale())
- Debugging specific errors (mainly guidance an indentation errors)
- Documentation help (structuring/mapping this README from Pycharm -> GitHub)

### Challenges along the way :
I ran into and fixed many indentation errors — the most common bug
throughout the project, since Python defines code blocks by spacing rather
than punctuation. I also struggled with my Git Commits. This stemmed from the fact that unfortuantley, my GitHub was never properly connected to my Pycharm repo. Committing was rather new to me, as i'd just upload files to my repo in previous assignements, adding commit messages locally rather than through the two softwares. This is something i really learnt along the way and want to improve moving forward. 

### External Resources :

- pygame.org/wiki/tutorials
- "The ultimate introduction to Pygame" by Clear Code on Youtube






